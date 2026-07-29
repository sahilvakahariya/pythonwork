from django.shortcuts import render
from myapp.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def add(request):
    if request.method == 'post':
        data=request.POST 
        title=data.get('title')
        author=data.get('author')
        price=data.get('price')

        book.objects.create(title=title,author=author,price=price)
        return render(request,'index.html',{'msg':"data succesfull thi gya !!!"})
   
    return render(request,'index.html')          
