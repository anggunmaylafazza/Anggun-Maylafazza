from django.urls import path
from .views import login_view, student_only_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('test-auth/student-only/', student_only_view),
]
