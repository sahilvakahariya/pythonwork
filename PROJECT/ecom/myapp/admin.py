from django.contrib import admin

from .models import (
    Category,
    Product,
    Wishlist,
)


# =========================================
# CATEGORY ADMIN
# =========================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# =========================================
# PRODUCT ADMIN
# =========================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "brand",
        "price",
        "discount_price",
        "stock",
        "is_available",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "is_available",
        "is_featured",
        "created_at",
    )

    search_fields = (
        "name",
        "brand",
        "sku",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


# =========================================
# WISHLIST ADMIN
# =========================================

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "product__name",
    )

    readonly_fields = (
        "created_at",
    )