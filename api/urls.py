from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditLogViewSet, health_check

router = DefaultRouter()
router.register(r'logs', AuditLogViewSet)

urlpatterns = [
    path('health/', health_check, name='health'),
    path('', include(router.urls))
]
