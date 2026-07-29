from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'is_public']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 13:
            raise forms.ValidationError("You must be older than 13 to create a profile.")
        return age