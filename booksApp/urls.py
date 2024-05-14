from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', BookListView.as_view(), name="book-list-view")
]