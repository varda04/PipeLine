from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from customer.models import ServiceType
from support.models import ServiceRequest

class DashboardViewTest(TestCase):
    def setUp(self):
        self.support_user = User.objects.create_user(username='staff', password='admin123', is_staff=True)
        self.client.login(username='staff', password='admin123')

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse('support:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/dashboard.html')

    def test_filter_pending_requests(self):
        service_type = ServiceType.objects.create(name='Other') 
        ServiceRequest.objects.create(customer=self.support_user, service_type= service_type, current_status='Pending')
        ServiceRequest.objects.create(customer=self.support_user, service_type= service_type, current_status='Resolved')

        response = self.client.get(reverse('support:dashboard'), {'status': 'Pending'})
        self.assertContains(response, 'Pending')
        self.assertNotIn("<td>Resolved</td>", response.content.decode())
        self.assertNotIn("<td>In Progress</td>", response.content.decode())

    def test_update_status_view(self):
        service_type = ServiceType.objects.create(name='Other') 
        req = ServiceRequest.objects.create(customer=self.support_user, service_type= service_type, current_status='Pending')
        response = self.client.post(reverse('support:update_status', args=[req.id]), {
            'new_status': 'Resolved'
        }, follow=True)
        req.refresh_from_db()
        self.assertEqual(req.current_status, 'Resolved')

    def test_non_staff_cannot_access_dashboard(self):
        normal_user = User.objects.create_user(username='normal', password='12345', is_staff= False)
        self.client.login(username='normal', password='12345')
        response = self.client.get(reverse('support:dashboard'))
        self.assertEqual(response.status_code, 302)