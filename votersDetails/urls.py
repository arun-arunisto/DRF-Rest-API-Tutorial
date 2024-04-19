from django.urls import path
from .views import VotersListView, VotersDetailView

urlpatterns = [
    path('voters-list/', VotersListView.as_view(), name='voters-list'),
    path('voter-detail/<int:pk>/', VotersDetailView.as_view(), name="voter-detail")
]