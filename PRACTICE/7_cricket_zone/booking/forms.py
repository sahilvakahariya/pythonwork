from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "name",
            "email",
            "mobile",
            "date",
            "time",
            "ball_type",
            "overs",
            "amount",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }),

            "mobile": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter mobile number"
            }),

            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),

            "ball_type": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ball type"
            }),

            "overs": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "1"
            }),

            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "readonly": "readonly"
            }),
        }