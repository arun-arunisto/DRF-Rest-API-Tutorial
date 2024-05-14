from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', BookListView.as_view(), name="book-list-view"),
    path('book-list-generic-view/', BookListGenericView.as_view(), name="book-list-generic-view"),
    path('author-list-generic-view/', AuthorListGenericView.as_view(), name='author-list-generic-view'),
    path('category-list-generic-view/', CategoryListGenericView.as_view(), name="category-list-generic-view")
]