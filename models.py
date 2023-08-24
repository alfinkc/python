from django.contrib import admin
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class places(models.Model):
    img = models.ImageField(upload_to='img/%y')
    name = models.CharField(max_length=100)
    def _str_(self):
        return self.name
