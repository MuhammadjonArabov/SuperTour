from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .forms import ApplicationForm
from rest_framework import viewsets, generics
from .models import Application
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicationSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


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


class ApplicationPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page_size"
    max_page_size = 100


class ApplicationStatusStatsAPIView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status']
    search_fields = ['full_name', 'phone_number', 'created_at']
    pagination_class = ApplicationPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'status_counts': self.status_count(),
                'applications': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status_counts': self.status_count(),
            'applications': serializer.data
        })

    def status_count(self):
        new_count = Application.objects.filter(status='new').count()
        old_count = Application.objects.filter(status='old').count()
        total_count = Application.objects.count()
        return {
            "new": new_count,
            "old": old_count,
            "total": total_count,
        }
