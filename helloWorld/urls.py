from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name="hello-world"),
    path('fetch-all-data/', views.fetch_all_data, name="fetch-all-data"),
    path("fetch-single-data/<int:id>/", views.fetch_single_data, name="fetch-single-data")
]