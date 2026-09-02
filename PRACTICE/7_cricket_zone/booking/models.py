from django.db import models


class Booking(models.Model):

    PAYMENT_METHODS = (
        ("Cash", "Cash"),
        ("Online", "Online"),
    )

    PAYMENT_STATUS = (
        ("Pending", "Pending"),
        ("Success", "Online Payment Successful"),
        ("Cash", "Cash"),
        ("Failed", "Failed"),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    date = models.DateField()

    time = models.CharField(max_length=20)

    ball_type = models.CharField(max_length=50)

    overs = models.IntegerField()

    amount = models.IntegerField()

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        default="Cash"
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time}"