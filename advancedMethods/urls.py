from django.urls import path
from advancedMethods.views import advanced_methods

urlpatterns =[
    path('advanced-methods/', advanced_methods, name='advanced-methods')
]
