from datetime import datetime
from django.db import models

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)  # optional
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now(), blank=True)

    # Returns name
    def __str__(self):
        return self.name
