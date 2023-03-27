from django.db import models

# Create your models here.

class Login(models.Model):
    # img: str
    img = models.ImageField(upload_to='pics')
    email = models.CharField(max_length=100)