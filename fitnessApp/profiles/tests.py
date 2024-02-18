from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['uuid', 'email', 'user']
        depth = 1 # This will include the user object details
