from django.contrib import admin
from .models import User,OrganizingComitee
# Register your models here.




@admin.register(OrganizingComitee)
class OrganizingComiteeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comitee_role', 'join_date', 'created_at', 'updated_at')
    search_fields = ('user', 'comitee_role')
    list_filter = ('comitee_role', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'affiliation', 'role', 'email', 'created_at', 'updated_at')
    search_fields = ('user_id', 'first_name', 'last_name', 'affiliation', 'role', 'email')
    list_filter = ('role', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')