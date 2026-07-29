from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    age = models.IntegerField()
    bio = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username