from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path('student-list/', student_list, name='student-list'),
    path('student-detail/<int:id>', student_detail, name="student-detail")
]