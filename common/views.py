from django.shortcuts import render
from .forms import ApplicationForm
from rest_framework import viewsets, generics
from .models import Application
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicationSerializers


def application_form_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'application_form.html', {'form': form, 'success_message': True})
        else:
            return render(request, 'application_form.html', {'form': form})
    else:
        form = ApplicationForm()

    return render(request, 'application_form.html', {'form': form})

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers

class ApplicationStatusStatsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        new_count = Application.objects.filter(status='new').count()
        old_count = Application.objects.filter(status='old').count()
        total_count = Application.objects.count()

        status_param = request.query_params.get('status', None)

        if status_param:
            applications = Application.objects.filter(status=status_param)
        else:
            applications = Application.objects.all()

        serializer = ApplicationSerializers(applications, many=True)

        return Response({
            'status_counts': {
                'new': new_count,
                'old': old_count,
                'total': total_count,
            },
            'applications': serializer.data
        })