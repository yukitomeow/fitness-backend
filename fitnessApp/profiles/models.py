from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255)
    cat = models.CharField(max_length=255, blank=True)
    # Assuming username and password are handled by the User model.

    def __str__(self):
        return self.user.username

