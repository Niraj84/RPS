from datetime import datetime
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    date= models.DateField(auto_now_add=True)
    result = models.CharField(max_length=5,null=True,blank=True)

    def __str__(self):
        return self.username
