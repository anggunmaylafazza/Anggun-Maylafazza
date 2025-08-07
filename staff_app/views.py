from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from auth_app.models import ArsysStaff
from auth_app.decorators import role_required
import traceback

@csrf_exempt
@role_required(['staff'])
def staff_profile_view(request):
    try:
        user_id = request.user_id
        staff = ArsysStaff.objects.get(user_id=user_id)

        if request.method == 'GET':
            return JsonResponse({
                'success': True,
                'data': {
                    'employee_id': staff.employee_id,
                    'first_name': staff.first_name,
                    'last_name': staff.last_name,
                    'phone_number': staff.phone,
                    'program_id': staff.program_id,
                    'specialization_id': staff.specialization_id,
                    'front_title': staff.front_title,
                    'rear_title': staff.rear_title,
                    'position_id': staff.position_id,
                    'structure_id': staff.structure_id,
                }
            })

        elif request.method == 'PUT':
            data = json.loads(request.body)

            staff.employee_id = data.get('employee_id')
            staff.first_name = data.get('first_name')
            staff.last_name = data.get('last_name')
            staff.phone = data.get('phone_number')
            staff.program_id = data.get('program_id')
            staff.specialization_id = data.get('specialization_id')
            staff.front_title = data.get('front_title')
            staff.rear_title = data.get('rear_title')
            staff.position_id = data.get('position_id')
            staff.structure_id = data.get('structure_id')
            staff.save()

            return JsonResponse({'success': True, 'message': 'Profil staff berhasil diperbarui'})

        else:
            return JsonResponse({'success': False, 'message': 'Method tidak diizinkan'}, status=405)

    except ArsysStaff.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Data staff tidak ditemukan'}, status=404)
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)
