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

class FileCountForm(forms.Form):
    file_count= forms.IntegerField(min_value=0, max_value=10, label="How many files would you like to attach?")