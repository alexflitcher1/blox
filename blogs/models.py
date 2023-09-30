from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Articles(models.Model):
    username = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    text = models.TextField()

class Users(AbstractUser):
    pass