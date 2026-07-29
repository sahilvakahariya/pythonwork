from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',index,name='index'),
    path('create',add,name='create'),
    path('display',display,name='display'),
    path('update',update,name='update'),
    path('delete',delete,name='delete')
]