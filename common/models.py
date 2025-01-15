from django.db import models
from django.core.exceptions import ValidationError
import re

class Application(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('old', 'Old'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def clean(self):
        phone_number = self.phone_number
        if not re.match(r'^\+998\d{9}$', phone_number):
            raise ValidationError({
                'phone_number': "Telefon raqami noto'g'ri formatda. To'g'ri format: +998xx xxx xx xx."
            })