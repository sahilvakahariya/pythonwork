from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [

    # Admin
    path("admin/", admin.site.urls),

    # Home
    path(
        "",
        views.home,
        name="home"
    ),

    # Booking
    path(
        "booking/",
        views.booking_page,
        name="booking"
    ),

    # Payment page
    path(
        "payment/<int:booking_id>/",
        views.payment_page,
        name="payment"
    ),

    # Cashfree return
    path(
        "payment/return/",
        views.payment_return,
        name="payment_return"
    ),

    # Payment success
    path(
        "payment/success/<int:booking_id>/",
        views.payment_success,
        name="payment_success"
    ),

    # Cashfree webhook
    path(
        "cashfree/webhook/",
        views.cashfree_webhook,
        name="cashfree_webhook"
    ),
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )