from django.shortcuts import render,redirect
from myapp.models import *
import os

# Create your views here.
def index(request):
    categories=category.objects.all()
    return render(request,'index.html',{"categories":categories})


def create(request):
    if request.method=='POST':
        data=request.POST
        id = data.get('id')
        name=data.get('name')
        price=data.get('price')
        qty=data.get('qty')
        cat=data.get('cat') 
        Category=category.objects.get(id=cat)
        image = request.FILES.get('image')


        if id:
            products=product.objects.get(id=id)
            products.name=name
            products.price=price
            products.qty=qty
            products.category=Category
            if request.FILES:
                if products.image:
                    os.remove(products.image.path)
                    products.image =image
            products.save()
            return redirect("display")

        else:
            product.objects.create(name=name,price=price,qty=qty,category=Category,image=image)

    return redirect('index') 

def display(request):
    products=product.objects.all()
    return render(request,"display.html",{"products":products})

def destroy(request):
    id = request.GET.get('id')

    if not id:
        return redirect("display")

    products = product.objects.filter(id=id).first()

    if not products:
        return redirect("display")

    if products.image:
        products.image.delete(save=False)

    products.delete()

    return redirect("display")

def retrive(request):
    id = request.GET['id']
    products = product.objects.get(id=id)
    categories = category.objects.all()
    all_products = product.objects.all()
    return render(request,"index.html",{'products':products,'categories':categories,'products':all_products})

