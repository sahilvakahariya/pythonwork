from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=20)


class Product(models.Model):
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()

    image = models.ImageField(upload_to='products/')

