from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from auth_app.models import (
    ArsysStudent,
    ArsysInstitutionFaculty,
    ArsysInstitutionClusterBase,
    ArsysInstitutionProgram,
    ArsysInstitutionSpecialization,
    ArsysStaff
)
from auth_app.decorators import role_required
import traceback

@csrf_exempt
@role_required(['student'])
def student_profile_view(request):
    try:
        user_id = request.user_id
        student = ArsysStudent.objects.get(user_id=user_id)

        # ambil fakultas & cluster berdasarkan foreign key dari program_id
        program = ArsysInstitutionProgram.objects.get(id=student.program_id)
        faculty = ArsysInstitutionFaculty.objects.get(id=program.faculty_id)
        cluster = ArsysInstitutionClusterBase.objects.get()

        if request.method == 'GET':
            return JsonResponse({
                'success': True,
                'data': {
                    'student_number': student.number,
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'phone_number': student.phone,
                    'program_study_id': student.program_id,
                    'specialization_id': student.specialization_id,
                    'supervisor_id': student.supervisor_id,
                    'faculty_name': faculty.name,     # hanya ditampilkan
                    'cluster_name': cluster.name      # hanya ditampilkan
                }
            })

        elif request.method == 'PUT':
            data = json.loads(request.body)

            student.number = data.get('student_number', student.number)
            student.first_name = data.get('first_name', student.first_name)
            student.last_name = data.get('last_name', student.last_name)
            student.phone = data.get('phone_number', student.phone)
            student.program_id = data.get('program_study_id', student.program_id)
            student.specialization_id = data.get('specialization_id', student.specialization_id)
            student.supervisor_id = data.get('supervisor_id', student.supervisor_id)
            student.save()

            return JsonResponse({'success': True, 'message': 'Profil mahasiswa berhasil diperbarui'})

        else:
            return JsonResponse({'success': False, 'message': 'Method tidak diizinkan'}, status=405)

    except ArsysStudent.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Data mahasiswa tidak ditemukan'}, status=404)
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)
