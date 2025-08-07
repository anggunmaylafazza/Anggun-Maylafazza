from django.urls import path
from .views import staff_profile_view

urlpatterns = [
    path('profile/', staff_profile_view),
]
