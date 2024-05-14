from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', BookListView.as_view(), name="book-list-view"),
    path('book-list-generic-view/', BookListGenericView.as_view(), name="book-list-generic-view")
]