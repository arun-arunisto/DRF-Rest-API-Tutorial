from django.urls import path
from server_health_check.views import *

urlpatterns = [
    path("health-check/", HealthCheckView.as_view(), name="server-health-check"),
    path("sentry-error-test-api-view/", TestAPIView.as_view(), name="sentry-test-api-view"),
]