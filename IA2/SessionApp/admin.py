from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'title', 'topic', 'session_day', 'start_time', 'end_time', 'room', 'created_at', 'updated_at')
    search_fields = ('title', 'topic', 'room')
    list_filter = ('session_day', 'conference')
    date_hierarchy = 'session_day'
    readonly_fields = ('created_at', 'updated_at')