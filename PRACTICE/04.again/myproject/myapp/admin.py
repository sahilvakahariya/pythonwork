from django.contrib import admin
from myapp.models import *

# Register your models here.
class BookDisplay(admin.ModelAdmin):
    list_display=('id','title','author','price')
admin.site.register(book, BookDisplay)  
