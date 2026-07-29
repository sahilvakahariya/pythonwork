from django.shortcuts import render
from myapp.models import *

def index(request):
    return render(request,'index.html')

def add(request):
    if request.method == 'post':
        data=request.POST
        name=data.get('name')
        rollno=data.get('rollno')
        marks=data.get('marks')

        student.objects.create(name=name,rollno=rollno,marks=marks)
        return render(request,'index.html',{'msg':'data added successfully'})
    return render(request,'index.html')   
