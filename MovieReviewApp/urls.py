from django.urls import path
from .views import *

urlpatterns = [
    path('movie-list-generic-view/', MovieListGenericView.as_view(), name='movie-list-generic-view'),
    path('movie-create-concrete-view/', MovieCreateConcreteView.as_view(), name='movie-create-concrete-view'),
    path('review-create-concrete-view/', ReviewCreateConcreteView.as_view(), name='review-create-concrete-view'),
    path('movie-list-concrete-view/', MovieListConcreteView.as_view(), name="movie-list-concrete-view"),
    path('review-list-concrete-view/', ReviewListConcreteView.as_view(), name="review-list-concrete-view"),
    path('movie-detail-concrete-view/<int:pk>/', MovieDetailConcreteView.as_view(), name="movie-detail-concrete-view"),
    path('review-detail-concrete-view/<int:pk>/', ReviewDetailConcreteView.as_view(), name="review-detail-concrete-view"),
    path('movie-delete-concrete-view/<int:pk>/', MovieDeleteConcreteView.as_view(), name="movie-delete-concrete-view"),
    path('review-delete-concrete-view/<int:pk>/', ReviewDeleteConcreteView.as_view(), name="review-delete-concrete-view"),
    path('movie-update-concrete-view/<int:pk>/', MovieUpdateConcreteView.as_view(), name="movie-update-concrete-view"),
    path('review-update-concrete-view/<int:pk>/', ReviewUpdateConcreteView.as_view(), name="review-update-concrete-view"),
    path('movie-list-create-concrete-view/', MovieListCreateConcreteView.as_view(), name="movie-list-create-concrete-view"),
    path('review-list-create-concrete-view/', ReviewListCreateConcreteView.as_view(), name="review-list-create-concrete-view"),
    path('movie-detail-update-concrete-view/<int:pk>/', MovieDetailUpdateConcreteView.as_view(), name="movie-detail-update-concrete-view"),
    path('review-detail-update-concrete-view/<int:pk>/', ReviewDetailUpdateConcreteView.as_view(), name="review-detail-update-concrete-view"),
    path('movie-detail-delete-concrete-view/<int:pk>/', MovieDetailDeleteConcreteView.as_view(), name="movie-detail-delete-concrete-view"),
    path('review-detail-delete-concrete-view/<int:pk>/', ReviewDetailDeleteConcreteView.as_view(), name="review-detail-delete-concrete-view"),

]