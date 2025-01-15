from django.contrib import admin
from common.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email', 'status', 'created_at')
    search_fields = ('full_name', 'phone_number', 'email')
    list_filter = ('full_name', 'phone_number', 'email', 'created_at')

