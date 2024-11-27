from django.urls import path
from .views import TodoListCreateView, TodoDetailView, DeleteAllTodosView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo_list_create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('delete-all/', DeleteAllTodosView.as_view(), name='delete_all_todos'),
]