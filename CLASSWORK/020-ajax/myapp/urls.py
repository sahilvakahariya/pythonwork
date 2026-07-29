from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",index,name="index"),
    path("test",test,name="test"),
    path("search",search,name="search"),
    path("countires",countires,name="countires"),
    path("states",states,name="states"),
    path("cities",cities,name="cities")
    
]