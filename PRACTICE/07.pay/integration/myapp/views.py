from django.shortcuts import render
import razorpay
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
# Create your views here.

def index(request):
    return render(request,"index.html")

def payment(request):
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_TDGjsasUwZeetX", "ZWuN6nNLPZcauqYErtleWKjU"))

    DATA = {
        "amount": amt*100,
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }
    payment = client.order.create(data=DATA)
    print(payment)
    return JsonResponse(payment)



def mail_send(request):

        data = request.POST

        to = data.get("to")
        subject = data.get("subject")
        message = data.get("message")

        send_mail(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to],
            fail_silently=False
        )

        return render(request, "index.html", {
            "msg": "✅ Email sent successfully!"
        })


def mail_html(request):
    html_message = render_to_string(
        "demo.html",
    )

    email = EmailMultiAlternatives(
        subject="Welcome",
        body="Your email client does not support HTML.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["sahilvakahariya@gmail.com"]
    )

    email.attach_alternative(html_message, "text/html")
    email.send()
    return HttpResponse("sent")


def mail_attach(request):
    email = EmailMessage(
        subject="Employee Report",
        body="Please find the attached report.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["sahilvakahariya@gmail.com"],
    )

    # Attach a file from your project
    email.attach_file("media/VID-20231024-WA0032.mp4")

    email.send()

    return HttpResponse("sent")

    