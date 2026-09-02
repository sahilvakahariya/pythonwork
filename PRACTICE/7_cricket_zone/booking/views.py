import base64
import io

from urllib.parse import quote
from datetime import datetime

import qrcode

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import escape

from .models import Booking


# =========================================================
# HOME
# =========================================================

def home(request):
    return render(
        request,
        "home.html"
    )


# =========================================================
# PRICE LIST
# =========================================================

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


# =========================================================
# CUSTOMER BOOKING OWNERSHIP
# =========================================================

def get_customer_booking(request, booking_id):

    customer_email = request.session.get(
        "customer_email"
    )

    customer_mobile = request.session.get(
        "customer_mobile"
    )

    if not customer_email or not customer_mobile:
        return None

    return Booking.objects.filter(
        id=booking_id,
        email=customer_email,
        mobile=customer_mobile
    ).first()


# =========================================================
# BOOKING
# =========================================================

def booking(request):

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
            "date",
            ""
        ).strip()

        time = request.POST.get(
            "time",
            ""
        ).strip()

        ball_type = request.POST.get(
            "ball_type",
            ""
        ).strip()

        overs = request.POST.get(
            "overs",
            ""
        ).strip()

        # =====================================================
        # VALIDATION
        # =====================================================

        if not all([
            name,
            email,
            mobile,
            date,
            time,
            ball_type,
            overs
        ]):

            messages.error(
                request,
                "Please fill all required fields."
            )

            return redirect("booking")

        # =====================================================
        # MOBILE VALIDATION
        # =====================================================

        if not mobile.isdigit() or len(mobile) != 10:

            messages.error(
                request,
                "Please enter a valid 10 digit mobile number."
            )

            return redirect("booking")

        # =====================================================
        # DATE VALIDATION
        # =====================================================

        try:

            booking_date = datetime.strptime(
                date,
                "%Y-%m-%d"
            ).date()

        except ValueError:

            messages.error(
                request,
                "Invalid booking date."
            )

            return redirect("booking")

        # =====================================================
        # OVERS
        # =====================================================

        try:

            overs = int(overs)

        except (ValueError, TypeError):

            messages.error(
                request,
                "Invalid overs selected."
            )

            return redirect("booking")

        # =====================================================
        # BALL TYPE
        # =====================================================

        if ball_type not in PRICES:

            messages.error(
                request,
                "Invalid ball type."
            )

            return redirect("booking")

        # =====================================================
        # OVERS VALIDATION
        # =====================================================

        if overs not in PRICES[ball_type]:

            messages.error(
                request,
                "Invalid overs selected."
            )

            return redirect("booking")

        # =====================================================
        # AMOUNT
        # =====================================================

        amount = PRICES[ball_type][overs]

        # =====================================================
        # VALID TIME SLOTS
        # 08:00 AM TO 11:45 PM
        # =====================================================

        valid_times = []

        for minutes in range(
            8 * 60,
            24 * 60,
            15
        ):

            hour = minutes // 60
            minute = minutes % 60

            if hour == 0:

                display_hour = 12
                ampm = "AM"

            elif hour < 12:

                display_hour = hour
                ampm = "AM"

            elif hour == 12:

                display_hour = 12
                ampm = "PM"

            else:

                display_hour = hour - 12
                ampm = "PM"

            valid_times.append(
                f"{display_hour}:{minute:02d} {ampm}"
            )

        if time not in valid_times:

            messages.error(
                request,
                "Invalid time slot."
            )

            return redirect("booking")

        # =====================================================
        # DUPLICATE SLOT
        # =====================================================

        already_booked = Booking.objects.filter(
            date=booking_date,
            time=time
        ).exists()

        if already_booked:

            messages.error(
                request,
                f"{time} is already booked. Please select another slot."
            )

            return redirect("booking")

        # =====================================================
        # CREATE BOOKING
        # =====================================================

        booking_obj = Booking.objects.create(

            name=name,

            email=email,

            mobile=mobile,

            date=booking_date,

            time=time,

            ball_type=ball_type,

            overs=overs,

            amount=amount,

            payment_method="Online",

            payment_status="Pending",
        )

        # =====================================================
        # SESSION
        # =====================================================

        request.session["customer_email"] = email

        request.session["customer_mobile"] = mobile

        request.session.modified = True

        # =====================================================
        # PAYMENT OPTIONS
        # =====================================================

        return redirect(
            "payment_options",
            booking_id=booking_obj.id
        )

    return render(
        request,
        "booking.html"
    )


# =========================================================
# PAYMENT OPTIONS
# =========================================================

def payment_options(request, booking_id):

    booking_obj = get_customer_booking(
        request,
        booking_id
    )

    if booking_obj is None:

        messages.error(
            request,
            "You are not authorized to access this booking."
        )

        return redirect(
            "my_bookings"
        )

    return render(
        request,
        "payment_options.html",
        {
            "booking": booking_obj
        }
    )


# =========================================================
# ONLINE UPI PAYMENT
# =========================================================

def online_payment(request, booking_id):

    booking_obj = get_customer_booking(
        request,
        booking_id
    )

    if booking_obj is None:

        messages.error(
            request,
            "You are not authorized to access this booking."
        )

        return redirect(
            "my_bookings"
        )

    # =====================================================
    # ALREADY SUCCESS
    # =====================================================

    if booking_obj.payment_status == "Success":

        return redirect(
            "home"
        )

    # =====================================================
    # KEEP PAYMENT PENDING
    # =====================================================

    booking_obj.payment_method = "Online"

    booking_obj.payment_status = "Pending"

    booking_obj.save(
        update_fields=[
            "payment_method",
            "payment_status"
        ]
    )

    # =====================================================
    # UPI DETAILS
    # =====================================================

    upi_id = settings.UPI_ID

    business_name = "7 Cricket Zone"

    amount = booking_obj.amount

    # =====================================================
    # TRANSACTION NOTE
    # =====================================================

    transaction_note = (
        f"7 Cricket Zone Booking #{booking_obj.id}"
    )

    # =====================================================
    # UPI URL
    # =====================================================

    upi_url = (
        "upi://pay?"
        f"pa={quote(str(upi_id))}"
        f"&pn={quote(business_name)}"
        f"&am={amount:.2f}"
        "&cu=INR"
        f"&tn={quote(transaction_note)}"
    )

    # =====================================================
    # GENERATE QR
    # =====================================================

    qr = qrcode.QRCode(

        version=None,

        error_correction=qrcode.constants.ERROR_CORRECT_H,

        box_size=10,

        border=4,
    )

    qr.add_data(
        upi_url
    )

    qr.make(
        fit=True
    )

    qr_image = qr.make_image(

        fill_color="black",

        back_color="white"
    )

    # =====================================================
    # BASE64
    # =====================================================

    buffer = io.BytesIO()

    qr_image.save(
        buffer,
        format="PNG"
    )

    qr_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode()

    # =====================================================
    # RENDER
    # =====================================================

    return render(

        request,

        "online_payment.html",

        {
            "booking": booking_obj,

            "upi_id": upi_id,

            "upi_url": upi_url,

            "qr_base64": qr_base64,

            "amount": amount,
        }
    )


# =========================================================
# ONLINE PAYMENT SUCCESS
# =========================================================

def online_payment_success(request, booking_id):

    if request.method != "POST":

        return redirect(
            "online_payment",
            booking_id=booking_id
        )

    booking_obj = get_customer_booking(
        request,
        booking_id
    )

    if booking_obj is None:

        messages.error(
            request,
            "Booking not found."
        )

        return redirect(
            "my_bookings"
        )

    # =====================================================
    # ALREADY SUCCESS
    # =====================================================

    if booking_obj.payment_status == "Success":

        return redirect(
            "home"
        )

    # =====================================================
    # ONLINE PAYMENT SUCCESS
    # =====================================================

    booking_obj.payment_method = "Online"

    booking_obj.payment_status = "Success"

    booking_obj.save(
        update_fields=[
            "payment_method",
            "payment_status"
        ]
    )

    # =====================================================
    # SEND CUSTOMER + OWNER EMAIL
    # =====================================================

    customer_sent, owner_sent = send_booking_emails(
        booking_obj
    )

    # =====================================================
    # MESSAGE
    # =====================================================

    if customer_sent:

        messages.success(
            request,
            "Online payment successful! Receipt sent to your email."
        )

    else:

        messages.warning(
            request,
            "Payment successful, but receipt email could not be sent."
        )

    # =====================================================
    # HOME
    # =====================================================

    return redirect(
        "home"
    )


# =========================================================
# PAYMENT CONFIRMATION BUTTON
# =========================================================

def payment_confirmation(request, booking_id):

    if request.method != "POST":

        return redirect(
            "online_payment",
            booking_id=booking_id
        )

    booking_obj = get_customer_booking(
        request,
        booking_id
    )

    if booking_obj is None:

        messages.error(
            request,
            "You are not authorized to access this booking."
        )

        return redirect(
            "my_bookings"
        )

    # =====================================================
    # CUSTOMER CONFIRMATION
    # =====================================================

    return redirect(
        "online_payment_success",
        booking_id=booking_id
    )


# =========================================================
# PAYMENT STATUS API
# =========================================================

def payment_status(request, booking_id):

    booking_obj = get_customer_booking(
        request,
        booking_id
    )

    if booking_obj is None:

        return JsonResponse(

            {
                "success": False,

                "error": "Unauthorized"
            },

            status=403
        )

    return JsonResponse(

        {
            "success": True,

            "booking_id": booking_obj.id,

            "payment_method":
                booking_obj.payment_method,

            "payment_status":
                booking_obj.payment_status,

            "amount":
                booking_obj.amount,
        }
    )


# =========================================================
# CUSTOMER PROFESSIONAL HTML RECEIPT EMAIL
# =========================================================

def send_booking_receipt(booking_obj):

    try:

        # =====================================================
        # PAYMENT STATUS
        # =====================================================

        if booking_obj.payment_status == "Success":

            payment_status_text = (
                "ONLINE PAYMENT SUCCESSFUL"
            )

            payment_status_color = "#198754"

            payment_status_bg = "#e8f7ee"

            payment_icon = "✓"

        elif booking_obj.payment_status == "Cash":

            payment_status_text = (
                "CASH PAYMENT"
            )

            payment_status_color = "#198754"

            payment_status_bg = "#e8f7ee"

            payment_icon = "✓"

        else:

            payment_status_text = (
                "PAYMENT PENDING"
            )

            payment_status_color = "#f59e0b"

            payment_status_bg = "#fff7e6"

            payment_icon = "!"

        # =====================================================
        # SAFE DATA
        # =====================================================

        customer_name = escape(
            str(booking_obj.name)
        )

        customer_email = escape(
            str(booking_obj.email)
        )

        customer_mobile = escape(
            str(booking_obj.mobile)
        )

        ball_type = escape(
            str(booking_obj.ball_type)
        )

        booking_time = escape(
            str(booking_obj.time)
        )

        payment_method = escape(
            str(booking_obj.payment_method)
        )

        booking_date = booking_obj.date.strftime(
            "%d %b %Y"
        )

        amount = f"₹{booking_obj.amount}"

        booking_id = f"#{booking_obj.id}"

        # =====================================================
        # SUBJECT
        # =====================================================

        subject = (
            f"7 Cricket Zone - "
            f"Booking Receipt {booking_id}"
        )

        # =====================================================
        # PLAIN TEXT EMAIL
        # =====================================================

        text_message = f"""

Hello {customer_name},

Thank you for booking with 7 Cricket Zone.

7 CRICKET ZONE
BOOKING RECEIPT

----------------------------------------

Booking ID      : {booking_id}

CUSTOMER DETAILS

Name            : {customer_name}
Email           : {customer_email}
Mobile          : {customer_mobile}

BOOKING DETAILS

Date            : {booking_date}
Time            : {booking_time}
Ball Type       : {ball_type}
Overs           : {booking_obj.overs}

PAYMENT DETAILS

Amount          : {amount}
Payment Method  : {payment_method}
Payment Status  : {payment_status_text}

----------------------------------------

IMPORTANT NOTES

Please arrive on time for your booking.
Carry your booking receipt with you.
Receipt is valid for the booked slot only.

Thank you for choosing 7 Cricket Zone.

Your Game, Our Passion 🏏

7 Cricket Zone

This is an automated receipt.

"""

        # =====================================================
        # HTML EMAIL
        # =====================================================

        html_message = f"""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta
name="viewport"
content="width=device-width, initial-scale=1.0"
>

<title>
7 Cricket Zone Booking Receipt
</title>

</head>


<body
style="
margin:0;
padding:0;
background:#eef1f7;
font-family:Arial,Helvetica,sans-serif;
color:#172033;
"
>


<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
background:#eef1f7;
padding:30px 10px;
"
>

<tr>

<td align="center">


<!-- =====================================================
     MAIN CONTAINER
===================================================== -->

<table
width="680"
cellspacing="0"
cellpadding="0"
border="0"
style="
max-width:680px;
width:100%;
background:#ffffff;
border-radius:18px;
overflow:hidden;
"
>


<!-- =====================================================
     HEADER
===================================================== -->

<tr>

<td
style="
background:#061a32;
padding:35px 20px 30px;
text-align:center;
border-bottom:5px solid #f5b82e;
"
>

<div
style="
font-size:32px;
font-weight:900;
letter-spacing:2px;
color:#f5b82e;
"
>
7 CRICKET ZONE
</div>


<div
style="
font-size:22px;
font-weight:700;
letter-spacing:3px;
color:#ffffff;
margin-top:8px;
"
>
BOOKING RECEIPT
</div>


<div
style="
font-size:14px;
color:#dbe4f0;
margin-top:12px;
"
>
Thank you for choosing 7 Cricket Zone 🏏
</div>

</td>

</tr>


<!-- =====================================================
     TOP BOOKING SUMMARY
===================================================== -->

<tr>

<td
style="
padding:25px 25px 10px;
"
>

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
background:#061a32;
border-radius:14px;
"
>

<tr>


<!-- BOOKING ID -->

<td
width="33%"
align="center"
style="
padding:20px 8px;
border-right:1px solid #40546d;
"
>

<div
style="
font-size:12px;
color:#b9c7d9;
"
>
BOOKING ID
</div>


<div
style="
font-size:25px;
font-weight:900;
color:#f5b82e;
margin-top:6px;
"
>
{booking_id}
</div>

</td>


<!-- DATE -->

<td
width="33%"
align="center"
style="
padding:20px 8px;
border-right:1px solid #40546d;
"
>

<div
style="
font-size:12px;
color:#b9c7d9;
"
>
BOOKING DATE
</div>


<div
style="
font-size:16px;
font-weight:700;
color:#ffffff;
margin-top:7px;
"
>
{booking_date}
</div>

</td>


<!-- TIME -->

<td
width="33%"
align="center"
style="
padding:20px 8px;
"
>

<div
style="
font-size:12px;
color:#b9c7d9;
"
>
BOOKING TIME
</div>


<div
style="
font-size:16px;
font-weight:700;
color:#ffffff;
margin-top:7px;
"
>
{booking_time}
</div>

</td>


</tr>

</table>

</td>

</tr>


<!-- =====================================================
     CONTENT
===================================================== -->

<tr>

<td
style="
padding:15px 25px 25px;
"
>


<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
>

<tr>


<!-- =====================================================
     LEFT COLUMN
===================================================== -->

<td
width="50%"
valign="top"
style="
padding-right:8px;
"
>


<!-- =====================================================
     CUSTOMER DETAILS
===================================================== -->

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
border:1px solid #dfe4eb;
border-radius:12px;
margin-bottom:15px;
"
>

<tr>

<td
style="
background:#0b2a4a;
color:#ffffff;
padding:14px;
font-size:15px;
font-weight:800;
"
>
👤 &nbsp; CUSTOMER DETAILS
</td>

</tr>


<tr>

<td
style="
padding:12px;
"
>

<table
width="100%"
cellspacing="0"
cellpadding="6"
border="0"
>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Name
</td>


<td
align="right"
style="
font-size:13px;
font-weight:700;
"
>
{customer_name}
</td>

</tr>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Email
</td>


<td
align="right"
style="
font-size:12px;
font-weight:600;
color:#1769e0;
word-break:break-all;
"
>
{customer_email}
</td>

</tr>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Mobile
</td>


<td
align="right"
style="
font-size:13px;
font-weight:700;
"
>
{customer_mobile}
</td>

</tr>


</table>

</td>

</tr>

</table>


<!-- =====================================================
     BOOKING DETAILS
===================================================== -->

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
border:1px solid #dfe4eb;
border-radius:12px;
margin-bottom:15px;
"
>

<tr>

<td
style="
background:#0b2a4a;
color:#ffffff;
padding:14px;
font-size:15px;
font-weight:800;
"
>
🏏 &nbsp; BOOKING DETAILS
</td>

</tr>


<tr>

<td
style="
padding:12px;
"
>

<table
width="100%"
cellspacing="0"
cellpadding="6"
border="0"
>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Date
</td>


<td
align="right"
style="
font-size:13px;
font-weight:700;
"
>
{booking_date}
</td>

</tr>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Time
</td>


<td
align="right"
style="
font-size:13px;
font-weight:700;
"
>
{booking_time}
</td>

</tr>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Ball Type
</td>


<td
align="right"
style="
font-size:13px;
font-weight:700;
"
>
{ball_type}
</td>

</tr>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Overs
</td>


<td
align="right"
style="
font-size:13px;
font-weight:700;
"
>
{booking_obj.overs}
</td>

</tr>


</table>

</td>

</tr>

</table>


<!-- =====================================================
     PAYMENT SUMMARY
===================================================== -->

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
border:1px solid #dfe4eb;
border-radius:12px;
"
>

<tr>

<td
style="
background:#0b2a4a;
color:#ffffff;
padding:14px;
font-size:15px;
font-weight:800;
"
>
₹ &nbsp; PAYMENT SUMMARY
</td>

</tr>


<tr>

<td
style="
padding:12px;
"
>

<table
width="100%"
cellspacing="0"
cellpadding="7"
border="0"
>


<tr>

<td
style="
font-size:14px;
font-weight:700;
"
>
Amount
</td>


<td
align="right"
style="
font-size:22px;
font-weight:900;
color:#e7a91e;
"
>
{amount}
</td>

</tr>


<tr>

<td
style="
border-top:1px dashed #cfd5dd;
padding-top:12px;
font-size:13px;
color:#687386;
"
>
Payment Method
</td>


<td
align="right"
style="
border-top:1px dashed #cfd5dd;
padding-top:12px;
font-size:13px;
font-weight:700;
"
>
{payment_method}
</td>

</tr>


<tr>

<td
style="
font-size:13px;
color:#687386;
"
>
Payment Status
</td>


<td
align="right"
>

<span
style="
display:inline-block;
background:{payment_status_bg};
border:1px solid {payment_status_color};
color:{payment_status_color};
padding:7px 9px;
border-radius:20px;
font-size:10px;
font-weight:900;
"
>

{payment_icon}

&nbsp;

{payment_status_text}

</span>

</td>

</tr>


</table>

</td>

</tr>

</table>


</td>


<!-- =====================================================
     RIGHT COLUMN
===================================================== -->

<td
width="50%"
valign="top"
style="
padding-left:8px;
"
>


<!-- =====================================================
     PAYMENT STATUS
===================================================== -->

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
border:1px solid #dfe4eb;
border-radius:12px;
margin-bottom:15px;
"
>

<tr>

<td
align="center"
style="
padding:30px 15px;
"
>


<div
style="
width:65px;
height:65px;
line-height:65px;
margin:auto;
border-radius:50%;
background:#198754;
color:#ffffff;
font-size:38px;
font-weight:bold;
"
>
{payment_icon}
</div>


<div
style="
margin-top:16px;
font-size:18px;
font-weight:900;
color:{payment_status_color};
"
>
{payment_status_text}
</div>


<div
style="
margin-top:8px;
font-size:12px;
line-height:20px;
color:#687386;
"
>
Your booking payment status has been
updated successfully.
</div>


</td>

</tr>

</table>


<!-- =====================================================
     IMPORTANT NOTES
===================================================== -->

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
background:#f1f5fb;
border-radius:12px;
margin-bottom:15px;
"
>

<tr>

<td
style="
padding:18px;
"
>


<div
style="
font-size:15px;
font-weight:900;
color:#0b2a4a;
margin-bottom:10px;
"
>
ⓘ &nbsp; IMPORTANT NOTES
</div>


<div
style="
font-size:12px;
line-height:24px;
color:#334155;
"
>

✓ Please arrive on time for your booking.<br>

✓ Carry your booking receipt with you.<br>

✓ Receipt is valid for the booked slot only.<br>

✓ For any query, contact 7 Cricket Zone.

</div>


</td>

</tr>

</table>


<!-- =====================================================
     NEED HELP
===================================================== -->

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
background:#061a32;
border-radius:12px;
"
>

<tr>

<td
align="center"
style="
padding:23px 12px;
"
>


<div
style="
font-size:18px;
font-weight:900;
color:#f5b82e;
"
>
☎ NEED HELP?
</div>


<div
style="
margin-top:9px;
font-size:12px;
color:#ffffff;
"
>
We're always here to assist you.
</div>


<div
style="
margin-top:8px;
font-size:12px;
color:#b9c7d9;
"
>
Contact 7 Cricket Zone for assistance.
</div>


</td>

</tr>

</table>


</td>

</tr>

</table>

</td>

</tr>


<!-- =====================================================
     THANK YOU
===================================================== -->

<tr>

<td
style="
padding:0 25px 25px;
"
>

<table
width="100%"
cellspacing="0"
cellpadding="0"
border="0"
style="
background:#f3f6fb;
border:1px solid #e0e6ef;
border-radius:12px;
"
>

<tr>

<td
align="center"
style="
padding:22px;
"
>


<div
style="
font-size:25px;
font-weight:900;
font-style:italic;
color:#e7a91e;
"
>
Thank You!
</div>


<div
style="
margin-top:7px;
font-size:14px;
color:#26364d;
line-height:22px;
"
>
We truly appreciate your trust in
<strong>7 Cricket Zone</strong>.
</div>


<div
style="
margin-top:5px;
font-size:13px;
color:#687386;
"
>
Keep playing, keep cheering! 🏏
</div>


</td>

</tr>

</table>

</td>

</tr>


<!-- =====================================================
     FOOTER
===================================================== -->

<tr>

<td
style="
background:#061a32;
padding:25px;
text-align:center;
border-top:4px solid #f5b82e;
"
>


<div
style="
font-size:19px;
font-weight:900;
color:#f5b82e;
letter-spacing:1px;
"
>
7 CRICKET ZONE
</div>


<div
style="
margin-top:7px;
font-size:13px;
color:#ffffff;
"
>
Your Game, Our Passion 🏏
</div>


<div
style="
margin-top:10px;
font-size:11px;
color:#aebed0;
"
>
Thank you for booking with us.
</div>


</td>

</tr>


</table>

</td>

</tr>

</table>


</body>

</html>

"""

        # =====================================================
        # SEND CUSTOMER EMAIL
        # =====================================================

        print(
            "CUSTOMER EMAIL:",
            booking_obj.email
        )

        print(
            "FROM EMAIL:",
            settings.DEFAULT_FROM_EMAIL
        )

        email_message = EmailMultiAlternatives(

            subject=subject,

            body=text_message,

            from_email=settings.DEFAULT_FROM_EMAIL,

            to=[
                booking_obj.email
            ],
        )

        email_message.attach_alternative(
            html_message,
            "text/html"
        )

        email_message.send(
            fail_silently=False
        )

        print(
            "CUSTOMER HTML RECEIPT SENT:",
            booking_obj.email
        )

        return True

    except Exception as e:

        print(
            "CUSTOMER EMAIL ERROR:",
            repr(e)
        )

        return False


# =========================================================
# OWNER NOTIFICATION
# =========================================================

def send_owner_notification(booking_obj):

    subject = (
        f"NEW BOOKING - "
        f"7 Cricket Zone #{booking_obj.id}"
    )

    # =====================================================
    # PAYMENT STATUS
    # =====================================================

    if booking_obj.payment_status == "Success":

        payment_status_text = (
            "Online Payment Successful"
        )

    else:

        payment_status_text = (
            booking_obj.payment_status
        )

    # =====================================================
    # OWNER EMAIL
    # =====================================================

    message = f"""

Hello Owner,

A new booking has been received.

========================================

             NEW BOOKING

========================================

Booking ID       : #{booking_obj.id}


CUSTOMER DETAILS

----------------------------------------

Name             : {booking_obj.name}

Email            : {booking_obj.email}

Mobile           : {booking_obj.mobile}


BOOKING DETAILS

----------------------------------------

Date             : {booking_obj.date}

Time             : {booking_obj.time}

Ball Type        : {booking_obj.ball_type}

Overs            : {booking_obj.overs}


PAYMENT DETAILS

----------------------------------------

Amount           : ₹{booking_obj.amount}

Payment Method   : {booking_obj.payment_method}

Payment Status   : {payment_status_text}


========================================

Please check Django Admin.

7 Cricket Zone

"""

    try:

        send_mail(

            subject=subject,

            message=message,

            from_email=settings.DEFAULT_FROM_EMAIL,

            recipient_list=[
                settings.OWNER_EMAIL
            ],

            fail_silently=False
        )

        print(
            "OWNER NOTIFICATION SENT:",
            settings.OWNER_EMAIL
        )

        return True

    except Exception as e:

        print(
            "OWNER EMAIL ERROR:",
            repr(e)
        )

        return False


# =========================================================
# SEND CUSTOMER + OWNER EMAILS
# =========================================================

def send_booking_emails(booking_obj):

    # Customer email first
    customer_sent = send_booking_receipt(
        booking_obj
    )

    # Owner email
    owner_sent = send_owner_notification(
        booking_obj
    )

    return (
        customer_sent,
        owner_sent
    )


# =========================================================
# CASH PAYMENT
# =========================================================

def cash_payment(request, booking_id):

    if request.method != "POST":

        return redirect(
            "payment_options",
            booking_id=booking_id
        )

    booking_obj = get_customer_booking(
        request,
        booking_id
    )

    if booking_obj is None:

        messages.error(
            request,
            "You are not authorized to access this booking."
        )

        return redirect(
            "my_bookings"
        )

    # =====================================================
    # CASH PAYMENT
    # =====================================================

    booking_obj.payment_method = "Cash"

    booking_obj.payment_status = "Cash"

    booking_obj.save(
        update_fields=[
            "payment_method",
            "payment_status"
        ]
    )

    # =====================================================
    # SEND EMAILS
    # =====================================================

    customer_sent, owner_sent = send_booking_emails(
        booking_obj
    )

    # =====================================================
    # MESSAGE
    # =====================================================

    if customer_sent:

        messages.success(
            request,
            "Cash booking confirmed! Receipt sent to your email."
        )

    else:

        messages.warning(
            request,
            "Cash booking confirmed, but customer receipt email could not be sent."
        )

    return redirect(
        "home"
    )


# =========================================================
# AVAILABLE SLOTS API
# =========================================================

def api_slots(request):

    selected_date = request.GET.get(
        "date",
        ""
    ).strip()

    if not selected_date:

        return JsonResponse(
            {
                "date": "",

                "booked_slots": [],
            }
        )

    # =====================================================
    # DATE VALIDATION
    # =====================================================

    try:

        selected_date_obj = datetime.strptime(
            selected_date,
            "%Y-%m-%d"
        ).date()

    except ValueError:

        return JsonResponse(

            {
                "date": selected_date,

                "booked_slots": [],

                "error": "Invalid date format."
            },

            status=400
        )

    # =====================================================
    # GET BOOKED SLOTS
    # =====================================================

    booked_slots = list(

        Booking.objects.filter(
            date=selected_date_obj
        ).values_list(
            "time",
            flat=True
        )
    )

    # =====================================================
    # CLEAN DUPLICATES
    # =====================================================

    booked_slots = list(

        dict.fromkeys(

            str(slot).strip()

            for slot in booked_slots

            if slot
        )
    )

    # =====================================================
    # RESPONSE
    # =====================================================

    return JsonResponse(

        {
            "date": selected_date,

            "booked_slots": booked_slots,
        }
    )


# =========================================================
# MY BOOKINGS
# =========================================================

def my_bookings(request):

    customer_email = request.session.get(
        "customer_email"
    )

    customer_mobile = request.session.get(
        "customer_mobile"
    )

    if not customer_email or not customer_mobile:

        messages.warning(
            request,
            "Please book a slot first."
        )

        return redirect(
            "booking"
        )

    bookings = Booking.objects.filter(

        email=customer_email,

        mobile=customer_mobile

    ).order_by(
        "-created_at"
    )

    return render(

        request,

        "my_bookings.html",

        {
            "bookings": bookings
        }
    )