from django.urls import path
from .views import student_profile_view

urlpatterns = [
    path('profile/', student_profile_view),
]
