from django.urls import path
from .views import health, create_resume

urlpatterns = [
    path('health/', health),
    path('resume/', create_resume),
] 