from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'action', 'entity_type', 'created_at')
    list_filter = ('action', 'created_at')
