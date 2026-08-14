from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "mobile",
        "date",
        "time",
        "ball_type",
        "overs",
        "amount",
        "payment_status",
        "created_at",
    )

    list_filter = (
        "date",
        "ball_type",
        "payment_status",
    )

    search_fields = (
        "name",
        "email",
        "mobile",
    )

    ordering = (
        "-created_at",
    )