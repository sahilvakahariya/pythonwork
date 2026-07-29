from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',index,name='index'),
    path('create',add,name='create'),
    path('display',display,name="display"),
     path('delete',delete_emplopyees,name="delete"),
    path('retrive',retrive,name="retrive")

]