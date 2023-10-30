from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Articles(models.Model):
    userid = models.IntegerField()
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class Users(AbstractUser):
    pass