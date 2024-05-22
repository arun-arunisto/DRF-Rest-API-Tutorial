from django.urls import path, include
from .views import *


urlpatterns = [
    path('recipe-list-create-view/', RecipeListCreateView.as_view(), name='recipe-list-create-view'),
]