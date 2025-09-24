
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'completed')
	list_filter = ('completed', 'created_at')
	search_fields = ('title',)
