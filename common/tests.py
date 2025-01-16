import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Application
from .forms import ApplicationForm
from .serializers import ApplicationSerializers

@pytest.mark.django_db
def test_application_form_valid():
    form_data = {
        'full_name': 'John Doe',
        'phone_number': '+998901234567',
        'email': 'john.doe@example.com'
    }
    form = ApplicationForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_application_form_invalid():
    form_data = {
        'full_name': '',
        'phone_number': '123456',  
        'email': 'invalid-email'  
    }
    form = ApplicationForm(data=form_data)
    assert not form.is_valid()
    assert 'phone_number' in form.errors
    assert 'email' in form.errors

# Test for ApplicationSerializers
def test_application_serializer_valid():
    valid_data = {
        'full_name': 'Jane Doe',
        'phone_number': '+998901234567',
        'email': 'jane.doe@example.com',
        'status': 'new',
    }
    serializer = ApplicationSerializers(data=valid_data)
    assert serializer.is_valid()

def test_application_serializer_invalid():
    invalid_data = {
        'full_name': 'Jane Doe',
        'phone_number': '12345',  
        'email': 'jane.doe@com',  
        'status': 'new',
    }
    serializer = ApplicationSerializers(data=invalid_data)
    assert not serializer.is_valid()
    assert 'phone_number' in serializer.errors
    assert 'email' in serializer.errors

@pytest.mark.django_db
def test_application_status_stats_api(client):
    Application.objects.create(full_name='User 1', phone_number='+998901234567', email='user1@example.com', status='new')
    Application.objects.create(full_name='User 2', phone_number='+998901234568', email='user2@example.com', status='old')

    url = reverse('application-status-stats')  
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert 'status_counts' in data
    assert 'applications' in data
    assert data['status_counts']['new'] == 1
    assert data['status_counts']['old'] == 1
    assert data['status_counts']['total'] == 2

@pytest.mark.django_db
def test_application_viewset(client):
    url = reverse('application-list') 
    application_data = {
        'full_name': 'Test User',
        'phone_number': '+998901234567',
        'email': 'testuser@example.com'
    }

    response = client.post(url, application_data, content_type='application/json')
    assert response.status_code == 201
    assert Application.objects.count() == 1

    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()) == 1

@pytest.mark.django_db
def test_application_form_view(client):
    url = reverse('application-form')  
    form_data = {
        'full_name': 'Test User',
        'phone_number': '+998901234567',
        'email': 'testuser@example.com'
    }

    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, data=form_data)
    assert response.status_code == 200
    assert Application.objects.count() == 1
