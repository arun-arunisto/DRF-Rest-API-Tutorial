from django.urls import path
from .views import BlogDetailView, BlogListView, CategoryDetailView, CategoryListView

urlpatterns = [
    path('blog-detail-view/', BlogDetailView.as_view(), name='blog-detail-view'),
    path('blog-list-view/<int:id>/', BlogListView.as_view(), name='blog-list-view'),
    path('category-detail-view/', CategoryDetailView.as_view(), name='category-detail-view'),
    path('category-list-view/<int:id>/', CategoryListView.as_view(), name='category-list-view')
]