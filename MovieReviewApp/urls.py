from django.urls import path
from .views import *

urlpatterns = [
    path('movie-list-generic-view/', MovieListGenericView.as_view(), name='movie-list-generic-view'),
    path('movie-create-concrete-view/', MovieCreateConcreteView.as_view(), name='movie-create-concrete-view'),
    path('review-create-concrete-view/', ReviewCreateConcreteView.as_view(), name='review-create-concrete-view'),
    path('movie-list-concrete-view/', MovieListConcreteView.as_view(), name="movie-list-concrete-view"),
    path('review-list-concrete-view/', ReviewListConcreteView.as_view(), name="review-list-concrete-view"),
    path('movie-detail-concrete-view/<int:pk>/', MovieDetailConcreteView.as_view(), name="movie-detail-concrete-view"),
    path('review-detail-concrete-view/<int:pk>/', ReviewDetailConcreteView.as_view(), name="review-detail-concrete-view")
]