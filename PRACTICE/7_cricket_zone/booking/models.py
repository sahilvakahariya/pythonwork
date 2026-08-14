from django.db import models


class Booking(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Success", "Success"),
        ("Failed", "Failed"),
    ]

    name = models.CharField(max_length=150)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    date = models.DateField()

    time = models.TimeField()

    ball_type = models.CharField(max_length=50)

    overs = models.IntegerField()

    amount = models.IntegerField()

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="Pending"
    )

    cashfree_order_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"#{self.id} - {self.name} - {self.date} - {self.time}"