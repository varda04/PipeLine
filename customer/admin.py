from django.contrib import admin
from .models import ServiceRequest, ServiceType, Attachment

admin.site.register(ServiceRequest)
admin.site.register(ServiceType)
admin.site.register(Attachment)