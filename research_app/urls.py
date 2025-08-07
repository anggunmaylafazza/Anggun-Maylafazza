from django.urls import path
from .views import student_research_view, student_edit_research_view, list_all_research, admin_detail_research, admin_update_research, assign_reviewer, staff_list_reviews, staff_respond_review_by_research, staff_view_research_detail

urlpatterns = [
    path('student', student_research_view),  # GET semua, POST upload
    path('student/<int:research_id>', student_edit_research_view),  # PUT update
    path('admin/all research', list_all_research),
    path('admin/<int:research_id>/', admin_detail_research),
    path('admin/milestone/<int:research_id>/', admin_update_research),
    path('admin/assign-reviewer/', assign_reviewer),
    path('staff/review', staff_list_reviews),
    path('staff/review/<int:research_id>', staff_respond_review_by_research),
    path('staff/<int:research_id>', staff_view_research_detail),

]
