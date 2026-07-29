from django.contrib import admin
from django.urls import path
from playlist.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),          # Home page
    path('music/', home),    # Music page
]