from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_form_view, name='application_form'),
]
