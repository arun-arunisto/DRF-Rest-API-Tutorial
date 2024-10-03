from django.urls import path
from server_health_check.views import *

urlpatterns = [
    path("health-check/", HealthCheckView.as_view(), name="server-health-check")
]