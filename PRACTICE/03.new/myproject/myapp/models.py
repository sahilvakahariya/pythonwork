from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
