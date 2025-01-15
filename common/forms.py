from django import forms
from .models import Application
from django.core.exceptions import ValidationError
import re


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'phone_number', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'F.I.O.'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Telefon raqamingiz'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+998\d{9}$', phone_number):
            raise ValidationError("Telefon raqami noto'g'ri formatda. To'g'ri format: +998xx xxx xx xx.")
        return phone_number