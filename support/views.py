from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from customer.models import ServiceRequest
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)
def support_dashboard(request):
    status = request.GET.get('status')
    if status:
        requests = ServiceRequest.objects.filter(current_status=status)
    else:
        requests = ServiceRequest.objects.all()

    return render(request, 'support/dashboard.html', {
        'requests': requests,
        'selected_status': status
    })


def support_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('support:dashboard')
        else:
            messages.error(request, "Invalid credentials or not a support staff user.")
    return render(request, 'support/login.html')

@user_passes_test(lambda u: u.is_staff)
def update_status(request, req_id):
    service_request = get_object_or_404(ServiceRequest, id=req_id)

    if request.method == 'POST':
        new_status = request.POST.get('new_status')

        if new_status:
            service_request.current_status = new_status
            service_request.save()

    # redirect back to the dashboard after updating the status
    return redirect('support:dashboard')