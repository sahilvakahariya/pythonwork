from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serilizer import *

# Create your views here.

@api_view(['POST'])
def create(request):
    return Response("POST API CALLING")

@api_view(['GET'])
def list(request):
    return Response("GET API CALLING")

@api_view(['PUT'])
def update(request):
    return Response("PUT API CALLING")

@api_view(['DELETE'])
def delete(request):
    return Response("DELETE API CALLING")

@api_view(['GET'])
def list_student(request):
    students = Student.objects.all()
    ser = StudentSeralizer(students,many=True)
    return Response({"data":ser.data})


@api_view(['POST'])
def create_student(request):
    ser = StudentSeralizer(data=request.data)
    if not  ser.is_valid():
        return Response({"errors":ser.errors,"message":"something went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data})
    
@api_view(['DELETE'])
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response("Student deleted")

@api_view(['PUT'])
def update_student(request,id):
    student = Student.objects.get(id=id)
    ser = StudentSeralizer(student,request.data)
    if not  ser.is_valid():
            return Response({"errors":ser.errors,"message":"something went wrong"})
    else:
            ser.save()
            return Response({"data":ser.data})
        


