from django.urls import path
from .views import TodoListView, TodoDetailView

urlpatterns = [
    path('todo-list/', TodoListView.as_view(), name="todo-list"),
    path('todo-details/<int:id>', TodoDetailView.as_view(), name='todo-details')
]