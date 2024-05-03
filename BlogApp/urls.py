from django.urls import path
from .views import BlogDetailView

urlpatterns = [
    path('blog-detail-view/', BlogDetailView.as_view(), name='blog-detail-view')
]