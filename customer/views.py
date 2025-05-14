from django.shortcuts import get_object_or_404, render, redirect
from .models import Attachment, ServiceType, ServiceRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.forms import modelformset_factory
from .forms import ServiceRequestForm, AttachmentForm, FileCountForm

@login_required
def customer_dashboard(request):
    return render(request, 'customer/dashboard.html')

def customer_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('customer:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'customer/signup.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        service_request_form = ServiceRequestForm(request.POST)

        if service_request_form.is_valid():
            service_request = service_request_form.save(commit=False)
            service_request.customer = request.user
            service_request.save()

            for uploaded_file in request.FILES.getlist('attachments'):
                Attachment.objects.create(request=service_request, file=uploaded_file)

            return redirect('customer:request_status')
    else:
        service_request_form = ServiceRequestForm()

    return render(request, 'customer/request_form.html', {
        'service_request_form': service_request_form
    })



@login_required
def track_requests(request):
    user_requests = ServiceRequest.objects.filter(customer=request.user)

    for req in user_requests:
        logs = req.status_logs.order_by('timestamp')
        req.submitted_at = logs.filter(status="Pending").first().timestamp if logs.filter(status="Pending").exists() else None
        req.resolved_at = logs.filter(status="Resolved").last().timestamp if logs.filter(status="Resolved").exists() else None
        req.resolution_duration = (req.resolved_at - req.submitted_at) if req.submitted_at and req.resolved_at else None

    return render(request, 'customer/request_status.html', {'requests': user_requests})
