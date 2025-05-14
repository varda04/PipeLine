from django.db import models
from django.contrib.auth.models import User
from customer.models import ServiceRequest

class RequestStatusHistory(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name="status_logs")
    status = models.CharField(max_length=50)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="status_updates")
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"Status change for Request #{self.request.id} by {self.updated_by.username} on {self.timestamp}"