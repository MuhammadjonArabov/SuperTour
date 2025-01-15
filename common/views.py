from django.shortcuts import render
from .forms import ApplicationForm
from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializers


def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'application_form.html', {'form': form, 'success_message': True})
    else:
        form = ApplicationForm()

    return render(request, 'application_form.html', {'form': form})


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers