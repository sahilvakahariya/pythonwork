from django.contrib import admin
from django.urls import path
from .views import home, explore, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),          # Home page
    path('home/', home, name='home'),
    path('explore/', explore, name='explore'),
    path('profile/', profile, name='profile'),
]