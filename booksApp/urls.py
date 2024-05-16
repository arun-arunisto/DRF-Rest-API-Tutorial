from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', BookListView.as_view(), name="book-list-view"),
    path('book-list-generic-view/', BookListGenericView.as_view(), name="book-list-generic-view"),
    path('author-list-generic-view/', AuthorListGenericView.as_view(), name='author-list-generic-view'),
    path('category-list-generic-view/', CategoryListGenericView.as_view(), name="category-list-generic-view"),
    path('book-detail-generic-view/<str:book_title>/', BookDetailGenericView.as_view(), name='book-detail-generic-view'),
    path('author-detail-generic-view/<int:pk>/', AuthorDetailGenericView.as_view(), name='author-detail-generic-view'),
    path('category-detail-generic-view/<int:pk>/', CategoryDetailGenericView.as_view(), name='category-detail-generic-view')
]