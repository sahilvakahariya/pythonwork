from django.urls import path

from .views import (
    home,
    booking,
    payment_options,
    online_payment,
    online_payment_success,
    payment_confirmation,
    payment_status,
    cash_payment,
    api_slots,
    my_bookings,
)

urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "booking/",
        booking,
        name="booking"
    ),

    path(
        "payment-options/<int:booking_id>/",
        payment_options,
        name="payment_options"
    ),

    path(
        "online-payment/<int:booking_id>/",
        online_payment,
        name="online_payment"
    ),

    path(
        "online-payment-success/<int:booking_id>/",
        online_payment_success,
        name="online_payment_success"
    ),

    path(
        "payment-confirmation/<int:booking_id>/",
        payment_confirmation,
        name="payment_confirmation"
    ),

    path(
        "payment-status/<int:booking_id>/",
        payment_status,
        name="payment_status"
    ),

    path(
        "cash-payment/<int:booking_id>/",
        cash_payment,
        name="cash_payment"
    ),

    path(
        "api/slots/",
        api_slots,
        name="api_slots"
    ),

    path(
        "my-bookings/",
        my_bookings,
        name="my_bookings"
    ),
]