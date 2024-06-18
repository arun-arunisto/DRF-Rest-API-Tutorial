from django.urls import path
from advancedMethods.views import *

urlpatterns =[
    #path('advanced-methods/', advanced_methods, name='advanced-methods')
    path('create-user/', create_user, name='create-user'),
    path('edit-user/<str:pk>/', edit_user, name='edit-user'),
]
