from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
]