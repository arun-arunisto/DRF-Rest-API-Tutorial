from django.urls import path
from .views import *

urlpatterns = [
    path('book-list-view/', book_list, name='book-list-view')
]