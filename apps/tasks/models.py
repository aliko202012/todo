from django.db import models
from apps.users.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)

    def _str_(self):
        return self.title