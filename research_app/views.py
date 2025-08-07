from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from auth_app.models import ArsysResearch, ArsysStudent, ArsysResearchReview, ArsysStaff
from auth_app.decorators import role_required
import traceback
import json

#STUDENT
@csrf_exempt
@role_required(['student'])
def student_research_view(request):
    try:
        user_id = request.user_id

        # Step 1: Cari student_id dari user_id
        student = ArsysStudent.objects.filter(user_id=user_id).first()
        if not student:
            return JsonResponse({'success': False, 'message': 'Data mahasiswa tidak ditemukan'}, status=404)

        # Step 2: Akses ArsysResearch berdasarkan student.id
        if request.method == 'GET':
            researches = ArsysResearch.objects.filter(student_id=student.id)
            if not researches.exists():
                return JsonResponse({'success': True, 'data': []})
            
            data = [{
                'id': r.id,
                'milestone_id': r.milestone_id,
                'academic_year_id': r.academic_year_id,
                'type_id': r.type_id,
                'student_id': r.student_id,
                'code': r.code,
                'status': r.status,
                'title': r.title,
                'abstract': r.abstract,
                'file': r.file
            } for r in researches]

            return JsonResponse({'success': True, 'data': data})

        elif request.method == 'POST':
            data = json.loads(request.body)

            title = data.get('title')
            abstract = data.get('abstract')
            file = data.get('file')
            type_id = data.get('type_id')

            if not all([title, abstract, file, type_id]):
                return JsonResponse({'success': False, 'message': 'Field wajib tidak lengkap'}, status=400)

            research = ArsysResearch.objects.create(
                student_id=student.id,
                title=title,
                abstract=abstract,
                file=file,
                type_id=type_id,
                milestone_id=1,
                academic_year_id=4  # ← samakan dengan data real kamu
            )

            return JsonResponse({'success': True, 'message': 'Proposal berhasil diupload', 'id': research.id})

        else:
            return JsonResponse({'success': False, 'message': 'Method tidak diizinkan'}, status=405)

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)



@csrf_exempt
@role_required(['student'])
def student_edit_research_view(request, research_id):
    try:
        user_id = request.user_id
        student = ArsysStudent.objects.filter(user_id=user_id).first()
        if not student:
            return JsonResponse({'success': False, 'message': 'Data mahasiswa tidak ditemukan'}, status=404)

        if request.method != 'PUT':
            return JsonResponse({'success': False, 'message': 'Method tidak diizinkan'}, status=405)

        research = ArsysResearch.objects.filter(id=research_id, student_id=student.id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Proposal tidak ditemukan'}, status=404)

        data = json.loads(request.body)
        research.title = data.get('title', research.title)
        research.abstract = data.get('abstract', research.abstract)
        research.file = data.get('file', research.file)
        research.save()

        return JsonResponse({'success': True, 'message': 'Proposal berhasil diperbarui'})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

#ADMIN
@csrf_exempt
@role_required(['admin'])
def list_all_research(request):
    try:
        if request.method != 'GET':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        all_research = ArsysResearch.objects.all()
        results = []

        for research in all_research:
            try:
                student = ArsysStudent.objects.get(id=research.student_id)
                student_name = f"{student.first_name} {student.last_name}".strip()
            except ArsysStudent.DoesNotExist:
                student_name = "Unknown"

            results.append({
                'id': research.id,
                'student_name': student_name,
                'milestone_id': research.milestone_id,
                'academic_year_id': research.academic_year_id,
                'type_id': research.type_id,
                'title': research.title,
                'abstract': research.abstract,
                'status': research.status,
                'file': research.file,
            })

        return JsonResponse({'success': True, 'data': results})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
@role_required(['admin'])
def admin_detail_research(request, research_id):
    try:
        if request.method != 'GET':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        research = ArsysResearch.objects.filter(id=research_id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Proposal tidak ditemukan'}, status=404)

        student = ArsysStudent.objects.filter(id=research.student_id).first()

        return JsonResponse({
            'success': True,
            'data': {
                'id': research.id,
                'student_id': research.student_id,
                'student_name': f"{student.first_name} {student.last_name}" if student else "-",
                'milestone_id': research.milestone_id,
                'academic_year_id': research.academic_year_id,
                'type_id': research.type_id,
                'status': research.status,
                'title': research.title,
                'abstract': research.abstract,
                'file': research.file,
                'code': research.code,
            }
        })

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
@role_required(['admin'])
def admin_update_research(request, research_id):
    try:
        if request.method != 'PUT':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        research = ArsysResearch.objects.filter(id=research_id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Proposal tidak ditemukan'}, status=404)

        data = json.loads(request.body)

        # Ambil milestone_id dari body request
        milestone_id = data.get('milestone_id')

        if milestone_id is None:
            return JsonResponse({'success': False, 'message': 'Milestone ID harus disertakan'}, status=400)

        research.milestone_id = milestone_id
        research.save()

        return JsonResponse({'success': True, 'message': 'Milestone proposal berhasil diperbarui'})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
@role_required(['admin'])
def assign_reviewer(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        research_id = data.get('research_id')
        reviewer_id = data.get('reviewer_id')

        if not research_id or not reviewer_id:
            return JsonResponse({'success': False, 'message': 'research_id dan reviewer_id wajib diisi'}, status=400)

        # Validasi: Research dan Reviewer harus ada
        from auth_app.models import ArsysResearch, ArsysStaff, ArsysResearchReview

        if not ArsysResearch.objects.filter(id=research_id).exists():
            return JsonResponse({'success': False, 'message': 'Proposal tidak ditemukan'}, status=404)

        if not ArsysStaff.objects.filter(id=reviewer_id).exists():
            return JsonResponse({'success': False, 'message': 'Reviewer tidak ditemukan'}, status=404)

        # Cek apakah reviewer sudah pernah ditugaskan
        if ArsysResearchReview.objects.filter(research_id=research_id, reviewer_id=reviewer_id).exists():
            return JsonResponse({'success': False, 'message': 'Reviewer sudah ditugaskan ke proposal ini'}, status=400)

        # Simpan ke database
        ArsysResearchReview.objects.create(
            research_id=research_id,
            reviewer_id=reviewer_id
        )

        return JsonResponse({'success': True, 'message': 'Reviewer berhasil ditugaskan'})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

#STAFF
@csrf_exempt
@role_required(['staff'])
def staff_list_reviews(request):
    try:
        user_id = request.user_id

        # Step 1: Temukan staff berdasarkan user_id
        staff = ArsysStaff.objects.filter(user_id=user_id).first()
        if not staff:
            return JsonResponse({'success': False, 'message': 'Staff tidak ditemukan'}, status=404)

        # Step 2: Ambil semua review yang ditugaskan ke staff ini
        reviews = ArsysResearchReview.objects.filter(reviewer_id=staff.id)

        # Step 3: Buat response
        data = [{
            'id': r.id,
            'research_id': r.research_id,
            'reviewer_id': r.reviewer_id,
            'decision_type': r.decision_id,
        } for r in reviews]

        return JsonResponse({'success': True, 'data': data})
    
    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)

@csrf_exempt
@role_required(['staff'])
def staff_view_research_detail(request, research_id):
    try:
        if request.method != 'GET':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        user_id = request.user_id

        # Step 1: Cek staff
        staff = ArsysStaff.objects.filter(user_id=user_id).first()
        if not staff:
            return JsonResponse({'success': False, 'message': 'Staff tidak ditemukan'}, status=404)

        # Step 2: Cek apakah research ini direview oleh staff tersebut
        review = ArsysResearchReview.objects.filter(research_id=research_id, reviewer_id=staff.id).first()
        if not review:
            return JsonResponse({'success': False, 'message': 'Anda tidak memiliki akses ke proposal ini'}, status=403)

        # Step 3: Ambil detail research
        research = ArsysResearch.objects.filter(id=research_id).first()
        if not research:
            return JsonResponse({'success': False, 'message': 'Proposal tidak ditemukan'}, status=404)

        # Step 4: Kembalikan data lengkap
        data = {
            'id': research.id,
            'student_id': research.student_id,
            'title': research.title,
            'abstract': research.abstract,
            'file': research.file,
            'type_id': research.type_id,
            'milestone_id': research.milestone_id,
            'academic_year_id': research.academic_year_id,
            'status': research.status,
            'code': research.code,
        }

        return JsonResponse({'success': True, 'data': data})

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)


@csrf_exempt
@role_required(['staff'])
def staff_respond_review_by_research(request, research_id):
    try:
        if request.method != 'PUT':
            return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

        user_id = request.user_id
        staff = ArsysStaff.objects.filter(user_id=user_id).first()
        if not staff:
            return JsonResponse({'success': False, 'message': 'Staff tidak ditemukan'}, status=404)

        # DEBUG: pastikan staff_id
        print("Staff ID:", staff.id)

        review = ArsysResearchReview.objects.filter(research_id=research_id, reviewer_id=staff.id).first()
        if not review:
            return JsonResponse({'success': False, 'message': 'Akses ditolak atau review tidak ditemukan'}, status=403)

        data = json.loads(request.body)
        decision_type_id = data.get('decision_type_id')

        if not decision_type_id:
            return JsonResponse({'success': False, 'message': 'Field decision_type_id wajib diisi'}, status=400)

        # DEBUG: cek id dan assignment
        print("Decision Type ID:", decision_type_id)
        print("Review ID:", review.id)

        review.decision_id = decision_type_id
        review.save()

        if int(decision_type_id) == 1:
            research = ArsysResearch.objects.filter(id=research_id).first()
            if research:
                research.milestone_id = 4
                research.save()

        return JsonResponse({'success': True, 'message': 'Review berhasil diperbarui'})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)