from django.db import models
from django.contrib.auth.models import User


# =========================================
# CATEGORY
# =========================================

class Category(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

  
    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# =========================================
# PRODUCT
# =========================================

class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    image_2 = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    image_3 = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    brand = models.CharField(
        max_length=100,
        blank=True
    )

    sku = models.CharField(
        max_length=100,
        unique=True
    )

    is_available = models.BooleanField(
        default=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    @property
    def final_price(self):

        if self.discount_price:
            return self.discount_price

        return self.price


# =========================================
# WISHLIST
# =========================================

class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist_items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlisted_by"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            "user",
            "product",
        )

        ordering = [
            "-created_at"
        ]

    def __str__(self):

        return f"{self.user.username} - {self.product.name}"