from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
  return render(request,"index.html")

def add(request):
    if request.method =='POST':
        data=request.POST
        id=data.get('id')
        name=data.get('name')
        price=data.get('price')
        qty=data.get('qty')
        
        if id:
            Product = product.objects.get(id=id)
            Product.name =name
            Product.price=price
            Product.qty=qty
            Product.save()
            return render(request,"index.html",{"msg":"update successfully"})
        
    else:
        product.objects.create(name=name,price=price,qty=qty)
        return render(request,"index.html",{"msg":"product successfully"})
    return redirect("display")
    
        
def display(request):
    products=product.objects.all() 
    return render(request,"display.html",{'products':products})   


def delete(request): 
    id=request.GET.get('id')
    Product=product.objects.get(id=id) 
    Product.delete()
    return redirect("display") 

def update(request):
    id=request.GET.get('id')
    products=product.objects.get(id=id) 
    return render(request,"index.html",{'products':products})
    
    