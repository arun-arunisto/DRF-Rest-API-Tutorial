from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('todo-list/', TodoListView.as_view(), name="todo-list")
]