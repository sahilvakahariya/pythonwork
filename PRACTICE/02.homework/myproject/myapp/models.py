from django.db import models

# Create your models here.
class student1(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    marks=models.IntegerField()
