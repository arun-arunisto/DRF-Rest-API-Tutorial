from django.urls import path
from advancedMethods.views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path('logout/', logout, name="logout"),
    path('hello-world/', hello_world, name='hello-world'),
    path('user-detail-view-auth/<int:pk>/', UserDetailViewAuth.as_view(), name='user-detail-view-auth'),
    path('upload-file/', upload_file, name='upload-file'),
    path('upload-file-class-view/', UploadFileClassView.as_view(), name="upload-file-class-view"),
    path('download-file/', download_file, name='download-file'),
    path('location-list-create-view/', LocationListCreateAPIView.as_view(), name="location-create-view"),
    path('location-detail-view/<int:pk>/', LocationRetrieveUpdateDestroyAPIView.as_view(), name="location-retrieve-view"),
    path('product-list-create-view/', ProductListCreateAPIView.as_view(), name="product-list-create-view"),
    path('product-detail-view/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-detail-view"),
    path('admin-list-create-view/', AdminUsersListCreateAPIView.as_view(), name="admin-list-create-view"),
    path("admin-detail-view/<int:pk>/", AdminUsersRetrieveUpdateDestroyAPIView.as_view(), name="admin-user-detail-view"),
    path("orders-list-create-view/", OrdersListCreateAPIView.as_view(),name="orders-list-create-view"),
    path("orders-detail-view/<int:pk>/", OrdersRetrieveUpdateDestroyAPIView.as_view(), name="orders-detail-view"),
    path('admin-user-login-view/', AdminLoginFormViewSet.as_view(), name="admin-loginform"),
    path('location-list-api-view/', LocationListAPIView.as_view(), name="location-list-api-view"),
    path('location-list-method/', LocationListAPIViewMethodDecoratorSpecific.as_view(), name="location-list-method"),
    path('orders-create-api-view/', OrdersListCreateAPIView.as_view(), name="order-create-api-view"),
    path('premium-users/', PremiumUsersListCreateAPIView.as_view(), name='premium-users'),
    path('premium-subscription/', PremiumSubscriptionListCreateAPIView.as_view(), name='premium-subscription'),
    path("bike-list-create", BikeListCreateView.as_view(), name="bike-list-create"),
    path("bike-model-list-create", BikeModelListCreateView.as_view(), name="bike-model-list-create"),
    path("booking-list-create", BookingListCreateView.as_view(), name="booking-list-create"),
    path("index-view", IndexView.as_view(), name="index-view"),
    path("image-upload-view", ImageUploadView.as_view(), name="image-upload-view")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
