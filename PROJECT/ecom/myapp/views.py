from rest_framework import viewsets

from .models import Category
from .serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all().order_by("-created_at")

    serializer_class = CategorySerializer