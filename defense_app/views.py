from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
import json
import traceback

from auth_app.models import ArsysStudent, ArsysResearch, ArsysEventApplicantDefense, ArsysStaff, ArsysDefenseApproval, ArsysResearchSupervisor, ArsysDefenseExaminer
from auth_app.decorators import role_required

#STUDENT
@csrf_exempt
@role_required(['student'])
def student_defense_submit(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        user_id = request.user_id

        # Step 1: Temukan student dari user_id
        student = ArsysStudent.objects.filter(user_id=user_id).first()
        if not student:
            return JsonResponse({'success': False, 'message': 'Data mahasiswa tidak ditemukan'}, status=404)

        # Step 2: Ambil payload dari body
        data = json.loads(request.body)
        research_id = data.get('research_id')
        defense_model_id = data.get('defense_model_id')  # 1 = predefense, 2 = public defense

        if not research_id or not defense_model_id:
            return JsonResponse({'success': False, 'message': 'Field research_id dan defense_model_id wajib diisi'}, status=400)

        # Step 3: Validasi kepemilikan research
        research = ArsysResearch.objects.filter(id=research_id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Research tidak ditemukan'}, status=404)
        if research.student_id != student.id:
            return JsonResponse({'success': False, 'message': 'Anda tidak memiliki akses ke research ini'}, status=403)

        # Step 4: Validasi milestone saat ini
        if int(defense_model_id) == 1 and research.milestone_id != 4:
            return JsonResponse({'success': False, 'message': 'Milestone saat ini tidak memenuhi syarat untuk mengajukan predefense'}, status=400)
        elif int(defense_model_id) == 2 and research.milestone_id != 10:
            return JsonResponse({'success': False, 'message': 'Milestone saat ini tidak memenuhi syarat untuk mengajukan public defense'}, status=400)

        # Step 5: Simpan data pengajuan ke ArsysEventApplicantDefense
        applicant_defense = ArsysEventApplicantDefense.objects.create(
            research_id=research.id,
            defense_model_id=defense_model_id
        )

        # Step 6: Tambahkan record di ArsysDefenseApproval (supervisor)
        # Ambil supervisor berdasarkan student_id
        supervisor_rel = ArsysResearchSupervisor.objects.filter(research_id=research.id).first()
        if not supervisor_rel:
            return JsonResponse({'success': False, 'message': 'Supervisor belum ditentukan untuk mahasiswa ini'}, status=400)

        supervisor_id = supervisor_rel.supervisor_id

        ArsysDefenseApproval.objects.create(
            research_id=research.id,
            defense_model_id=defense_model_id,
            approver_id=supervisor_id,
            approver_role=1  # Supervisor
        )

        # Step 7: Update milestone
        if int(defense_model_id) == 1:
            research.milestone_id = 5  # pengajuan predefense
        elif int(defense_model_id) == 2:
            research.milestone_id = 11  # pengajuan public defense
        research.save()

        return JsonResponse({
            'success': True,
            'message': 'Pengajuan berhasil dikirim',
            'event_applicant_defense_id': str(applicant_defense.id)
        })

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

@csrf_exempt
@role_required(['student'])
def student_defense_status(request):
    try:
        if request.method != 'GET':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        user_id = request.user_id

        # Step 1: Temukan student dari user_id
        student = ArsysStudent.objects.filter(user_id=user_id).first()
        if not student:
            return JsonResponse({'success': False, 'message': 'Data mahasiswa tidak ditemukan'}, status=404)

        # Step 2: Temukan research milik student
        research = ArsysResearch.objects.filter(student_id=student.id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Belum ada data research'}, status=404)

        # Step 3: Ambil data event_applicant_defense
        defense_application = ArsysEventApplicantDefense.objects.filter(research_id=research.id).first()
        if not defense_application:
            return JsonResponse({'success': True, 'data': {
                'research_id': research.id,
                'milestone_id': research.milestone_id,
                'defense_model_id': None,
                'event_applicant_defense_id': None,
                'approval': None,
            }})

        # Step 4: Cek approval dari supervisor (jika ada)
        approval = ArsysDefenseApproval.objects.filter(research_id=research.id).first()

        approval_data = None
        if approval:
            # Ambil informasi staff
            staff = ArsysStaff.objects.filter(id=approval.approver_id).first()
            approval_data = {
                'approver_id': approval.approver_id,
                'approver_code': staff.code if staff else None,
                'approver_role': approval.approver_role,
                'decision_type_id': approval.decision,
            }

        # Step 5: Susun response
        return JsonResponse({'success': True, 'data': {
            'research_id': research.id,
            'milestone_id': research.milestone_id,
            'defense_model_id': defense_application.defense_model_id,
            'event_applicant_defense_id': str(defense_application.id),
            'approval': approval_data,
        }})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)


#STAFF
@csrf_exempt
@role_required(['staff'])
def supervisor_list_defense_requests(request):
    try:
        user_id = request.user_id

        staff = ArsysStaff.objects.filter(user_id=user_id).first()
        if not staff:
            return JsonResponse({'success': False, 'message': 'Staff tidak ditemukan'}, status=404)

        # Ambil semua approval sebagai supervisor (approver_role = 1)
        approvals = ArsysDefenseApproval.objects.filter(
            approver_id=staff.id,
            approver_role=1
        )

        result = []
        for approval in approvals:
            research = ArsysResearch.objects.filter(id=approval.research_id).first()
            if not research:
                continue

            student = ArsysStudent.objects.filter(id=research.student_id).first()
            if not student:
                continue

            result.append({
                'id': approval.id,
                'research_id': research.id,
                'student_name': f"{student.first_name} {student.last_name}",
                'defense_model_id': approval.defense_model_id,
                'decision': approval.decision,
                'milestone_id': research.milestone_id,
                'title': research.title,
                'abstract': research.abstract,
                'file': research.file
            })

        return JsonResponse({'success': True, 'data': result})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

@csrf_exempt
@role_required(['staff'])
def supervisor_get_defense_detail(request, research_id):
    try:
        if request.method != 'GET':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        user_id = request.user_id

        # Step 1: Temukan staff dari user_id
        staff = ArsysStaff.objects.filter(user_id=user_id).first()
        if not staff:
            return JsonResponse({'success': False, 'message': 'Staff tidak ditemukan'}, status=404)

        # Step 2: Cek apakah staff adalah supervisor dari research_id ini
        is_supervisor = ArsysResearchSupervisor.objects.filter(
            research_id=research_id,
            supervisor_id=staff.id
        ).exists()

        if not is_supervisor:
            return JsonResponse({'success': False, 'message': 'Anda tidak memiliki akses ke research ini'}, status=403)

        # Step 3: Ambil detail research
        research = ArsysResearch.objects.filter(id=research_id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Research tidak ditemukan'}, status=404)

        student = ArsysStudent.objects.filter(id=research.student_id).first()
        applicant = ArsysEventApplicantDefense.objects.filter(research_id=research.id).first()

        result = {
            'research_id': research.id,
            'student_name': f"{student.first_name} {student.last_name}" if student else None,
            'title': research.title,
            'abstract': research.abstract,
            'file': research.file,
            'milestone_id': research.milestone_id,
            'defense_model_id': applicant.defense_model_id if applicant else None
        }

        return JsonResponse({'success': True, 'data': result})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)


@csrf_exempt
@role_required(['staff'])
def supervisor_approve_defense(request, research_id):
    try:
        if request.method != 'PUT':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        user_id = request.user_id
        staff = ArsysStaff.objects.filter(user_id=user_id).first()
        if not staff:
            return JsonResponse({'success': False, 'message': 'Staff tidak ditemukan'}, status=404)

        # Validasi apakah dia supervisor dari research ini
        is_supervisor = ArsysResearchSupervisor.objects.filter(
            research_id=research_id,
            supervisor_id=staff.id
        ).exists()

        if not is_supervisor:
            return JsonResponse({'success': False, 'message': 'Anda bukan supervisor dari research ini'}, status=403)

        # Ambil approval untuk research ini dan role 1 (supervisor)
        approval = ArsysDefenseApproval.objects.filter(
            research_id=research_id,
            approver_id=staff.id,
            approver_role=1
        ).first()

        if not approval:
            return JsonResponse({'success': False, 'message': 'Data approval tidak ditemukan'}, status=404)

        data = json.loads(request.body)
        decision = data.get('decision')

        if decision is None:
            return JsonResponse({'success': False, 'message': 'Field decision wajib diisi'}, status=400)

        # Simpan keputusan supervisor
        approval.decision = decision
        approval.save()

        # Jika decision == 1 (setuju), periksa defense_model_id untuk update milestone
        research = ArsysResearch.objects.filter(id=research_id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Research tidak ditemukan'}, status=404)

        if decision == 1:
            if approval.defense_model_id == 1 and research.milestone_id == 5:
                # Predefense setuju -> milestone 6
                research.milestone_id = 6
                research.save()

            elif approval.defense_model_id == 2 and research.milestone_id == 11:
                # Public defense -> cek apakah ada 2 persetujuan: supervisor (1) dan approver lain (3)
                approvals = ArsysDefenseApproval.objects.filter(
                    research_id=research_id,
                    defense_model_id=2,
                    decision=1
                )

                roles = approvals.values_list('approver_role', flat=True)

                if 1 in roles and 3 in roles:
                    # Kedua approver sudah menyetujui → milestone 12
                    research.milestone_id = 12
                    research.save()

        return JsonResponse({'success': True, 'message': 'Keputusan berhasil disimpan'})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

#ADMIN
@csrf_exempt
@role_required(['admin'])
def admin_list_defense_approvals(request):
    try:
        approvals = ArsysDefenseApproval.objects.all()

        result = []
        for approval in approvals:
            research = ArsysResearch.objects.filter(id=approval.research_id).first()
            student = ArsysStudent.objects.filter(id=research.student_id).first()
            if not research or not student:
                continue

            result.append({
                'id': approval.id,
                'research_id': research.id,
                'student_name': f"{student.first_name} {student.last_name}",
                'defense_model_id': approval.defense_model_id,
                'approver_id': approval.approver_id,
                'approver_role': approval.approver_role,
                'decision': approval.decision,
            })

        return JsonResponse({'success': True, 'data': result})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

@csrf_exempt
@role_required(['admin'])
def admin_set_defense_schedule(request, approval_id):
    try:
        if request.method != 'PUT':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        data = json.loads(request.body)
        event_id = data.get('event_id')
        session_id = data.get('session_id')
        space_id = data.get('space_id')

        if not all([event_id, session_id, space_id]):
            return JsonResponse({'success': False, 'message': 'Semua field wajib diisi'}, status=400)

        approval = ArsysDefenseApproval.objects.filter(id=approval_id).first()
        if not approval:
            return JsonResponse({'success': False, 'message': 'Data approval tidak ditemukan'}, status=404)

        applicant = ArsysEventApplicantDefense.objects.filter(research_id=approval.research_id).first()
        if not applicant:
            return JsonResponse({'success': False, 'message': 'Applicant tidak ditemukan'}, status=404)

        applicant.event_id = event_id
        applicant.session_id = session_id
        applicant.space_id = space_id
        applicant.save()

        # Update milestone
        research = ArsysResearch.objects.filter(id=approval.research_id).first()
        if research:
            if research.milestone_id == 6:
                research.milestone_id = 7
            elif research.milestone_id == 12:
                research.milestone_id = 13
            research.save()

        return JsonResponse({'success': True, 'message': 'Jadwal berhasil disimpan'})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

@csrf_exempt
@role_required(['admin'])
def admin_assign_examiner(request, applicant_id):
    try:
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        data = json.loads(request.body)
        examiner_id = data.get('examiner_id')

        if not examiner_id:
            return JsonResponse({'success': False, 'message': 'examiner_id wajib diisi'}, status=400)

        applicant = ArsysEventApplicantDefense.objects.filter(id=applicant_id).first()
        if not applicant:
            return JsonResponse({'success': False, 'message': 'Data applicant tidak ditemukan'}, status=404)

        ArsysDefenseExaminer.objects.create(
        applicant_id=applicant_id,
        examiner_id=examiner_id
)

        # Update milestone
        research = ArsysResearch.objects.filter(id=applicant.research_id).first()
        if research:
            if research.milestone_id == 7:
                research.milestone_id = 10
            elif research.milestone_id == 13:
                research.milestone_id = 16  
            research.save()

        return JsonResponse({'success': True, 'message': 'Examiner berhasil ditambahkan'})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)
