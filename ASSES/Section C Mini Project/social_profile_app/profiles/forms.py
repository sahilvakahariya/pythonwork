from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'bio', 'is_public']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 13:
            raise forms.ValidationError("User must be older than 13.")
        return age