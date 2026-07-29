from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from ecom.models import *
from ecom.serilizer import *

# Create your views here.

class Categories(APIView):
    def get(self,request):
        Categories
