from django.db import models

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    cuisine = models.ForeignKey(
        Cuisine,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='foods/')
    description = models.TextField()

    def __str__(self):
        return self.name