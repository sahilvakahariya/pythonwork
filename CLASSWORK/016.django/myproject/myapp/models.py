from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    phone=models.CharField(max_length=100,null=True)

class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField() 
    brand=models.CharField(max_length=100,null=True)
    description=models.TextField(default="No description")

