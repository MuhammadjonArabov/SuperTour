from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, application_form_view, ApplicationStatusStatsAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'api', ApplicationViewSet, basename='application')

schema_view = get_schema_view(
    openapi.Info(
        title="SuperTour API",
        default_version='v1',
        description="API documentation for the SuperTour application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@super-tour.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'common'

urlpatterns = [
    path('', application_form_view, name='application_form'),

    path('api/applications/', ApplicationStatusStatsAPIView.as_view(), name='application-list'),

    path('api/', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
