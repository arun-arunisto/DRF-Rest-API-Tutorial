from django.urls import path
from .views import *

urlpatterns = [
    path('movie-list-generic-view/', MovieListGenericView.as_view(), name='movie-list-generic-view'),
    path('movie-create-concrete-view/', MovieCreateConcreteView.as_view(), name='movie-create-concrete-view')
]