from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.TextField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, null=True)