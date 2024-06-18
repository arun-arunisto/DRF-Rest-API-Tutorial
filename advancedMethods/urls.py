from django.urls import path
from advancedMethods.views import *

urlpatterns =[
    #path('advanced-methods/', advanced_methods, name='advanced-methods')
    path('create-user/', create_user, name='create-user'),
    path('edit-user/<str:pk>/', edit_user, name='edit-user'),
    path('user-list-view/', UserListView.as_view(), name='user-detail-view'),
    path('user-detail-view/<int:pk>/', UserDetailView.as_view(), name='user-detail-view'),
    path('login-view/', login_view, name='login-view'),
    path('login-class-view/', LoginView.as_view(), name='login-class-view'),
    path('login-class-viewset/', LoginViewSet.as_view(), name='login-class-viewset'),
    path('login-n-generate/', LoginNGenerate.as_view(), name='login-n-generate'),
    path('logout/', logout, name="logout")
]
