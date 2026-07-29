from django.contrib import admin
from .models import Student1

class studentAdmin(admin.ModelAdmin):
    list_display = ['name', 'rollno', 'marks']

admin.site.register(Student1, studentAdmin)


