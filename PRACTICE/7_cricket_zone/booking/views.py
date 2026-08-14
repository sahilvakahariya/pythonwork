import json
import uuid
import base64
import hmac
import hashlib

import requests

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db import IntegrityError, transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Booking


# ============================================================
# PRICE
# ============================================================

PRICES = {

    "Tennis Ball": {
        5: 99,
        10: 150,
        15: 200,
        20: 250,
        30: 299,
        40: 399,
    },

    "PU Ball": {
        5: 120,
        10: 180,
        15: 250,
        20: 300,
        30: 349,
        40: 499,
    },
}


# ============================================================
# SLOT GENERATOR
# ============================================================

def generate_slots():

    from datetime import datetime, timedelta

    slots = []

    start = datetime.strptime(
        "08:00",
        "%H:%M"
    )

    end = datetime.strptime(
        "23:45",
        "%H:%M"
    )

    current = start

    while current <= end:

        hour = current.hour

        if hour < 12:
            period = "Morning"

        elif hour < 17:
            period = "Afternoon"

        elif hour < 20:
            period = "Evening"

        else:
            period = "Night"

        slots.append({
            "value": current.strftime("%H:%M"),
            "display": current.strftime("%I:%M %p"),
            "period": period,
        })

        current += timedelta(minutes=15)

    return slots


# ============================================================
# HOME
# ============================================================

def home(request):

    return render(
        request,
        "home.html"
    )


# ============================================================
# BOOKING PAGE
# ============================================================

def booking_page(request):

    slots = generate_slots()

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        mobile = request.POST.get(
            "mobile",
            ""
        ).strip()

        date = request.POST.get(
            "date"
        )

        time = request.POST.get(
            "time"
        )

        ball_type = request.POST.get(
            "ball_type"
        )

        overs_value = request.POST.get(
            "overs"
        )

        # ====================================================
        # BASIC VALIDATION
        # ====================================================

        if not all([
            name,
            email,
            mobile,
            date,
            time,
            ball_type,
            overs_value
        ]):

            messages.error(
                request,
                "Please fill all booking details."
            )

            return render(
                request,
                "booking.html",
                {
                    "slots": slots
                }
            )

        # ====================================================
        # OVERS
        # ====================================================

        try:

            overs = int(
                overs_value
            )

        except ValueError:

            messages.error(
                request,
                "Invalid overs selected."
            )

            return render(
                request,
                "booking.html",
                {
                    "slots": slots
                }
            )

        # ====================================================
        # PRICE
        # ====================================================

        try:

            amount = PRICES[
                ball_type
            ][overs]

        except KeyError:

            messages.error(
                request,
                "Invalid ball or overs selected."
            )

            return render(
                request,
                "booking.html",
                {
                    "slots": slots
                }
            )

        # ====================================================
        # DOUBLE BOOKING PROTECTION
        # ====================================================

        try:

            with transaction.atomic():

                existing = (
                    Booking.objects
                    .select_for_update()
                    .filter(
                        date=date,
                        time=time,
                        payment_status__in=[
                            "Pending",
                            "Success"
                        ]
                    )
                    .first()
                )

                if existing:

                    messages.error(
                        request,
                        "Sorry! This slot is already booked. Please select another slot."
                    )

                    return render(
                        request,
                        "booking.html",
                        {
                            "slots": slots
                        }
                    )

                booking = Booking.objects.create(

                    name=name,

                    email=email,

                    mobile=mobile,

                    date=date,

                    time=time,

                    ball_type=ball_type,

                    overs=overs,

                    amount=amount,

                    payment_status="Pending"

                )

        except IntegrityError:

            messages.error(
                request,
                "This slot was just booked by another customer. Please select another slot."
            )

            return render(
                request,
                "booking.html",
                {
                    "slots": slots
                }
            )

        # ====================================================
        # CASHFREE ORDER
        # ====================================================

        try:

            order_id = (
                f"7CZ_{booking.id}_"
                f"{uuid.uuid4().hex[:12]}"
            )

            headers = {

                "x-client-id":
                    settings.CASHFREE_CLIENT_ID,

                "x-client-secret":
                    settings.CASHFREE_CLIENT_SECRET,

                "x-api-version":
                    settings.CASHFREE_API_VERSION,

                "Content-Type":
                    "application/json",

                "Accept":
                    "application/json",
            }

            base_url = (
                request.build_absolute_uri("/")
            )

            # =================================================
            # RETURN URL
            # =================================================

            return_url = (

                base_url.rstrip("/")

                + reverse(
                    "payment_return"
                )

                + f"?booking_id={booking.id}"

                + f"&order_id={order_id}"
            )

            # =================================================
            # WEBHOOK URL
            # =================================================

            notify_url = (

                base_url.rstrip("/")

                + reverse(
                    "cashfree_webhook"
                )
            )

            # =================================================
            # CASHFREE PAYLOAD
            # =================================================

            payload = {

                "order_id":
                    order_id,

                "order_amount":
                    float(amount),

                "order_currency":
                    "INR",

                "customer_details": {

                    "customer_id":
                        f"customer_{booking.id}",

                    "customer_name":
                        name,

                    "customer_email":
                        email,

                    "customer_phone":
                        mobile,
                },

                "order_meta": {

                    "return_url":
                        return_url,

                    "notify_url":
                        notify_url,
                },

                "order_note":
                    f"7 Cricket Zone Booking #{booking.id}",
            }

            # =================================================
            # CREATE ORDER
            # =================================================

            response = requests.post(

                settings.CASHFREE_BASE_URL
                + "/orders",

                headers=headers,

                json=payload,

                timeout=30
            )

            try:

                data = response.json()

            except Exception:

                data = {}

            # =================================================
            # CASHFREE ERROR
            # =================================================

            if response.status_code not in [
                200,
                201
            ]:

                booking.delete()

                print(
                    "CASHFREE ERROR:",
                    response.text
                )

                messages.error(
                    request,
                    "Payment gateway error. Please try again."
                )

                return render(
                    request,
                    "booking.html",
                    {
                        "slots": slots
                    }
                )

            # =================================================
            # PAYMENT SESSION
            # =================================================

            payment_session_id = data.get(
                "payment_session_id"
            )

            if not payment_session_id:

                booking.delete()

                messages.error(
                    request,
                    "Payment session could not be created."
                )

                return render(
                    request,
                    "booking.html",
                    {
                        "slots": slots
                    }
                )

            # =================================================
            # SAVE CASHFREE ORDER ID
            # =================================================

            booking.cashfree_order_id = (
                order_id
            )

            booking.save(
                update_fields=[
                    "cashfree_order_id"
                ]
            )

            # =================================================
            # PAYMENT PAGE
            # =================================================

            return render(
                request,
                "payment.html",
                {
                    "booking":
                        booking,

                    "payment_session_id":
                        payment_session_id,

                    "cashfree_mode":
                        "sandbox",
                }
            )

        except Exception as e:

            print(
                "PAYMENT SETUP ERROR:",
                e
            )

            booking.delete()

            messages.error(
                request,
                "Payment setup failed. Please try again."
            )

            return render(
                request,
                "booking.html",
                {
                    "slots": slots
                }
            )

    # ========================================================
    # GET REQUEST
    # ========================================================

    return render(
        request,
        "booking.html",
        {
            "slots": slots
        }
    )


# ============================================================
# PAYMENT PAGE
# /payment/21/
# ============================================================

def payment_page(
    request,
    booking_id
):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    # ========================================================
    # ALREADY PAID
    # ========================================================

    if booking.payment_status == "Success":

        return redirect(
            "payment_success",
            booking_id=booking.id
        )

    # ========================================================
    # PAYMENT PAGE
    # ========================================================

    return render(
        request,
        "payment.html",
        {
            "booking": booking,
            "payment_session_id": "",
            "cashfree_mode": "sandbox",
        }
    )


# ============================================================
# GET CASHFREE PAYMENT STATUS
# ============================================================

def get_cashfree_payment_status(
    order_id
):

    headers = {

        "x-client-id":
            settings.CASHFREE_CLIENT_ID,

        "x-client-secret":
            settings.CASHFREE_CLIENT_SECRET,

        "x-api-version":
            settings.CASHFREE_API_VERSION,

        "Accept":
            "application/json",
    }

    try:

        response = requests.get(

            settings.CASHFREE_BASE_URL
            + f"/orders/{order_id}/payments",

            headers=headers,

            timeout=30
        )

    except Exception as e:

        print(
            "CASHFREE STATUS ERROR:",
            e
        )

        return None

    if response.status_code != 200:

        print(
            "CASHFREE STATUS RESPONSE:",
            response.text
        )

        return None

    try:

        payments = response.json()

    except Exception:

        return None

    if not isinstance(
        payments,
        list
    ):

        return None

    # ========================================================
    # SUCCESS
    # ========================================================

    for payment in payments:

        if payment.get(
            "payment_status"
        ) == "SUCCESS":

            return "SUCCESS"

    # ========================================================
    # PENDING
    # ========================================================

    for payment in payments:

        if payment.get(
            "payment_status"
        ) == "PENDING":

            return "PENDING"

    # ========================================================
    # FAILED
    # ========================================================

    return "FAILED"


# ============================================================
# SEND BOOKING RECEIPT
# ============================================================

def send_booking_receipt(
    booking
):

    owner_email = getattr(
        settings,
        "OWNER_EMAIL",
        None
    )

    subject = (
        f"7 Cricket Zone - "
        f"Booking Confirmed #{booking.id}"
    )

    text_content = f"""
7 CRICKET ZONE
BOOKING RECEIPT

Booking ID: #{booking.id}

Customer: {booking.name}

Email: {booking.email}

Mobile: {booking.mobile}

Date: {booking.date}

Time: {booking.time.strftime("%I:%M %p")}

Ball: {booking.ball_type}

Overs: {booking.overs}

Amount: ₹{booking.amount}

Payment Status: SUCCESS

Thank you for booking with 7 Cricket Zone.
"""

    html_content = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

</head>

<body style="
font-family:Arial;
background:#f5f5f5;
padding:30px;
">

<div style="
max-width:600px;
margin:auto;
background:white;
padding:30px;
border-radius:15px;
">

<h2 style="color:#198754;">
🏏 7 Cricket Zone
</h2>

<h3>
Booking Confirmed
</h3>

<hr>

<p>
<b>Booking ID:</b>
#{booking.id}
</p>

<p>
<b>Customer:</b>
{booking.name}
</p>

<p>
<b>Email:</b>
{booking.email}
</p>

<p>
<b>Mobile:</b>
{booking.mobile}
</p>

<p>
<b>Date:</b>
{booking.date}
</p>

<p>
<b>Time:</b>
{booking.time.strftime("%I:%M %p")}
</p>

<p>
<b>Ball:</b>
{booking.ball_type}
</p>

<p>
<b>Overs:</b>
{booking.overs}
</p>

<p>
<b>Amount:</b>
₹{booking.amount}
</p>

<p style="
background:#d1e7dd;
padding:12px;
border-radius:8px;
color:#0f5132;
">

<b>
Payment Status: SUCCESS
</b>

</p>

<p>
Thank you for booking with
<b>7 Cricket Zone</b>.
</p>

</div>

</body>

</html>
"""

    recipients = [
        booking.email
    ]

    if owner_email:

        recipients.append(
            owner_email
        )

    email = EmailMultiAlternatives(

        subject=subject,

        body=text_content,

        from_email=settings.DEFAULT_FROM_EMAIL,

        to=recipients
    )

    email.attach_alternative(
        html_content,
        "text/html"
    )

    email.send(
        fail_silently=False
    )


# ============================================================
# PAYMENT RETURN
# ============================================================

def payment_return(request):

    booking_id = request.GET.get(
        "booking_id"
    )

    order_id = request.GET.get(
        "order_id"
    )

    if not booking_id:

        return redirect(
            "home"
        )

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    # ========================================================
    # ORDER ID
    # ========================================================

    if not order_id:

        order_id = (
            booking.cashfree_order_id
        )

    if not order_id:

        return render(
            request,
            "payment_failed.html",
            {
                "booking": booking,
                "error":
                    "Cashfree order ID not found."
            }
        )

    # ========================================================
    # VERIFY PAYMENT
    # ========================================================

    status = get_cashfree_payment_status(
        order_id
    )

    # ========================================================
    # SUCCESS
    # ========================================================

    if status == "SUCCESS":

        if booking.payment_status != "Success":

            booking.payment_status = (
                "Success"
            )

            booking.save(
                update_fields=[
                    "payment_status"
                ]
            )

            try:

                send_booking_receipt(
                    booking
                )

            except Exception as e:

                print(
                    "EMAIL ERROR:",
                    e
                )

        return redirect(
            "payment_success",
            booking_id=booking.id
        )

    # ========================================================
    # PENDING
    # ========================================================

    if status == "PENDING":

        return render(
            request,
            "payment_pending.html",
            {
                "booking": booking
            }
        )

    # ========================================================
    # FAILED
    # ========================================================

    booking.payment_status = (
        "Failed"
    )

    booking.save(
        update_fields=[
            "payment_status"
        ]
    )

    return render(
        request,
        "payment_failed.html",
        {
            "booking": booking
        }
    )


# ============================================================
# PAYMENT SUCCESS
# ============================================================

def payment_success(
    request,
    booking_id
):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    if booking.payment_status != "Success":

        return redirect(
            "home"
        )

    return render(
        request,
        "payment_success.html",
        {
            "booking": booking
        }
    )


# ============================================================
# CASHFREE WEBHOOK
# ============================================================

@csrf_exempt
@require_POST
def cashfree_webhook(request):

    try:

        raw_body = request.body

        signature = request.headers.get(
            "x-webhook-signature"
        )

        timestamp = request.headers.get(
            "x-webhook-timestamp"
        )

        # ====================================================
        # SIGNATURE CHECK
        # ====================================================

        if not signature or not timestamp:

            return HttpResponse(
                "Missing signature",
                status=400
            )

        signed_payload = (
            timestamp.encode()
            + raw_body
        )

        expected_signature = (
            base64.b64encode(
                hmac.new(
                    settings.CASHFREE_CLIENT_SECRET.encode(),
                    signed_payload,
                    hashlib.sha256
                ).digest()
            ).decode()
        )

        if not hmac.compare_digest(
            signature,
            expected_signature
        ):

            return HttpResponse(
                "Invalid signature",
                status=401
            )

        # ====================================================
        # JSON
        # ====================================================

        data = json.loads(
            raw_body
        )

        # ====================================================
        # ORDER ID
        # ====================================================

        order_id = (
            data.get(
                "data",
                {}
            )
            .get(
                "order",
                {}
            )
            .get(
                "order_id"
            )
        )

        # ====================================================
        # PAYMENT STATUS
        # ====================================================

        payment_status = (
            data.get(
                "data",
                {}
            )
            .get(
                "payment",
                {}
            )
            .get(
                "payment_status"
            )
        )

        if not order_id:

            return HttpResponse(
                "No order id",
                status=400
            )

        # ====================================================
        # BOOKING
        # ====================================================

        try:

            booking = Booking.objects.get(
                cashfree_order_id=order_id
            )

        except Booking.DoesNotExist:

            return HttpResponse(
                "Booking not found",
                status=404
            )

        # ====================================================
        # SUCCESS ONLY
        # ====================================================

        if payment_status == "SUCCESS":

            if booking.payment_status != "Success":

                booking.payment_status = (
                    "Success"
                )

                booking.save(
                    update_fields=[
                        "payment_status"
                    ]
                )

                try:

                    send_booking_receipt(
                        booking
                    )

                except Exception as e:

                    print(
                        "WEBHOOK EMAIL ERROR:",
                        e
                    )

        return HttpResponse(
            "OK",
            status=200
        )

    except Exception as e:

        print(
            "WEBHOOK ERROR:",
            e
        )

        return HttpResponse(
            "Webhook error",
            status=500
        )