from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    lang=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    address=models.TextField()