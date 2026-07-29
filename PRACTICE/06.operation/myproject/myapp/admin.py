from django.contrib import admin
from myapp.models import *

# Register your models here
class productdisplay(admin.ModelAdmin):
    list_display=['id','name','price','qty']
    
admin.site.register(product,productdisplay)    

