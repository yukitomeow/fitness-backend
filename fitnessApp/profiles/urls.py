from django.urls import path
from .views import RegisterUserAPIView

urlpatterns = [
    path('api/register/', RegisterUserAPIView.as_view(), name='api_register'),
    # Add other app-specific routes here
]