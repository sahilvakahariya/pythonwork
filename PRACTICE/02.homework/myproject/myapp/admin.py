from django.contrib import admin
from .models import *

# Register your models here.
class studentdisplay(admin.ModelAdmin):
    list_display=['name','rollno','marks']
admin.site.register(student1,studentdisplay)