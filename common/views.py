# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm


def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'application_form.html', {'form': form, 'success_message': True})
    else:
        form = ApplicationForm()

    return render(request, 'application_form.html', {'form': form})
