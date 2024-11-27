from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'created_at', 'age')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('created_at', 'age')
    ordering = ('created_at',)