from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('blog-detail-view/', BlogDetailView.as_view(), name='blog-detail-view'),
    path('blog-list-view/<int:id>/', BlogListView.as_view(), name='blog-list-view')
]