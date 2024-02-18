from django.urls import path
from .views import RegisterUserAPIView

urlpatterns = [
    path('api/', name='api'),
    # Add other app-specific routes here
]