from django.db import models

class AuditLog(models.Model):
    ACTIONS = (('create', 'Create'), ('update', 'Update'), ('delete', 'Delete'), ('view', 'View'))
    user_id = models.IntegerField(db_index=True)
    action = models.CharField(max_length=20, choices=ACTIONS)
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    changes = models.JSONField(default=dict)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'audit_logs'
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.action} {self.entity_type} by user {self.user_id}"
