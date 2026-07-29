from django.db import models


# Create your models here.

class person(models.Model):
    name=models.CharField(max_length=100)

class passport(models.Model):
    person=models.OneToOneField(person,on_delete=models.CASCADE)
    country=models.CharField(max_length=20)  
    pid=models.CharField(max_length=20)  

class category(models.Model):
    name=models.CharField(max_length=100)

class product(models.Model):
    category= models.ForeignKey('category', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.FloatField()
    qty=models.IntegerField()
    image =models.ImageField(upload_to="images",null=True)

    def total(self):
        return self.price*self.qty


class book(models.Model):
    name=models.CharField(max_length=100)

class author(models.Model):
    book=models.ManyToManyField(book)
    name=models.CharField(max_length=100)
             