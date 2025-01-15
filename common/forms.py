from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'phone_number', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'F.I.O.'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Telefon raqamingiz'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
        }