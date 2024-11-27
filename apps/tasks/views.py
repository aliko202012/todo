from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class DeleteAllTodosView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        Todo.objects.filter(user=request.user).delete()
        return Response({"message": "All tasks deleted successfully."})