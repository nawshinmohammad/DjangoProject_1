from django.contrib import admin
from .models import Tasks

# Register your models here.

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title','owner','created_at')
    list_filter = ('created_at',)
    search_fields = ('task_title', 'description')
