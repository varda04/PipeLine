from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from customer.models import ServiceRequest
from .models import RequestStatusHistory

_old_status = {}

@receiver(pre_save, sender=ServiceRequest)
def cache_old_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            _old_status[instance.pk] = old_instance.current_status
        except sender.DoesNotExist:
            _old_status[instance.pk] = None

@receiver(post_save, sender=ServiceRequest)
def create_initial_status(sender, instance, created, **kwargs):
    if created:
        RequestStatusHistory.objects.create(
            request=instance,
            status=instance.current_status,
            updated_by=instance.customer,
            note="Initial status set automatically."
        )

@receiver(post_save, sender=ServiceRequest)
def create_status_history_on_update(sender, instance, created, **kwargs):
    if not created:
        previous_status = _old_status.get(instance.pk)
        if previous_status and previous_status != instance.current_status:
            RequestStatusHistory.objects.create(
                request=instance,
                status=instance.current_status,
                updated_by=instance.customer,
                note="Status updated"
            )
        # Clean up to prevent memory bloat
        _old_status.pop(instance.pk, None)
