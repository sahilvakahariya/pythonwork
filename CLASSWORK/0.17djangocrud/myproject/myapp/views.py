from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def add(request):
    if request.method == 'POST':
        data = request.POST
        id = data.get('id')
        name=data.get('name')
        rollno=data.get('rollno')
        marks=data.get('marks')

        if id:
            student=Student1.objects.get(id=id)
            student.name=name
            student.rollno=rollno
            student.marks=marks
            student.save()
            return render(request,"index.html",{"msg":"update thi jase !!!"})

        else:  

            Student1.objects.create(name=name,rollno=rollno,marks=marks)
            return render(request,'index.html',{"msg":"regristration successfully"})

    return render(request,'index.html')


def display(request):
    students = Student1.objects.all()
    return render(request, 'display.html', {'students': students})


def delete_student(request):
    id = request.GET.get("id")
    student=Student1.objects.get(id=id)
    student.delete()
    return redirect("display")   


def retrive(request):
    id = request.GET.get("id")
    student=Student1.objects.get(id=id)
    return render(request,"index.html",{"student":student})
