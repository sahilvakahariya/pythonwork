from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def add(request):
    if request.method=='POST':   
        data=request.POST
        id=data.get('id')
        name=data.get('name')
        phone=data.get('phone')
        salary=data.get('salary')

        employee.objects.create(id=id,name=name,phone=phone,salary=salary)
        return render(request,'index.html',{"msg":"regristration successfully !!!!!"})

    return render(request,"index.html")

def display(request):
    employees = employee.objects.all()
    return render(request, 'display.html', {'employees': employees})   


def delete_emplopyees(request):
    id = request.GET.get("id")
    employees=employee.objects.get(id=id)
    employees.delete()
    return redirect("display")   


def retrive(request):
    id = request.GET.get("id")
    employees=employee.objects.get(id=id)
    return render(request,"index.html",{"employees":employees})