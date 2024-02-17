from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Import DRF components
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, ProfileSerializer

def register_user(request):
    if request.method == 'POST':
        # Assuming you have a form that captures user information
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Create the User
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Create the Profile
        Profile.objects.create(user=user, email=email)
        
        # Redirect or respond appropriately
        # return redirect('some-view-name')

# New API view
class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            profile = Profile.objects.create(user=user, email=user.email)
            profile_serializer = ProfileSerializer(profile)
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
