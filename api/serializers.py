from rest_framework import serializers
from .models import AuditLog

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ('id', 'user_id', 'action', 'entity_type', 'entity_id', 'changes', 'ip_address', 'created_at')
        read_only_fields = ('id', 'created_at')
