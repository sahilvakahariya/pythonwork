from django.db import models


# Create your models here.
class book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
