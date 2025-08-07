from django.urls import path
from defense_app.views import student_defense_submit, supervisor_approve_defense, student_defense_status, supervisor_list_defense_requests, supervisor_get_defense_detail, admin_assign_examiner, admin_list_defense_approvals, admin_set_defense_schedule

urlpatterns = [
    path('student/submit-defense', student_defense_submit),
    path('student/',student_defense_status),
    path('staff/supervisor/defense-list/', supervisor_list_defense_requests),
    path('staff/supervisor/defense/<int:research_id>/', supervisor_get_defense_detail),
    path('staff/supervisor/<int:research_id>/approval', supervisor_approve_defense),
    path('admin/defense/approval/', admin_list_defense_approvals),
    path('admin/defense/approval/<int:approval_id>/set_schedule', admin_set_defense_schedule),
    path('admin/defense/approval/<int:applicant_id>/assign_examiner', admin_assign_examiner),
]
