from django import forms
from .models import ServiceRequest, Attachment

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']