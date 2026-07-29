
from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def add(request):
    if request.method=='POST':
        data=request.POST
        id=data.get('id')
        name=data.get('name')
        age=data.get('age')
        email=data.get('email')
    
        if id:  #update mate
            students=student.objects.get(id=id)
            students.name=name
            students.age=age
            students.email=email
            students.save()
            return render(request,'index.html',{'msg':'data update thi gya che'})

        else:
            student.objects.create(name=name,age=age,email=email)
    return render(request,'index.html',{'msg':'registration successfull'})


def display(request):
    students=student.objects.all()
    return render(request,'display.html',{'students':students})

def delete(request):
    id=request.GET.get('id')
    students=student.objects.get(id=id)
    students.delete()
    return redirect('display')

def update(request):
    id=request.GET.get('id')
    students=student.objects.get(id=id)
    return render(request,'index.html',{'students':students})
    




