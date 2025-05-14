from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from customer.models import ServiceRequest, ServiceType

class CustomerAccessTests(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='customer1', password='pass123', is_staff=False)
        self.service_type = ServiceType.objects.create(name='Internet')
        self.request = ServiceRequest.objects.create(
            customer=self.customer,
            service_type=self.service_type,
            current_status='Pending'
        )

    def test_customer_login_success(self):
        logged_in = self.client.login(username='customer1', password='pass123')
        self.assertTrue(logged_in)

    def test_customer_cannot_access_support_dashboard(self):
        self.client.login(username='customer1', password='pass123')
        response = self.client.get(reverse('support:dashboard'))
        self.assertEqual(response.status_code, 302)  # Redirect to login (default behavior of @user_passes_test)
        self.assertIn('/customer/login/', response.url)

    def test_customer_can_see_own_request_details(self):
        self.client.login(username='customer1', password='pass123')
        response = self.client.get(reverse('customer:request_status'))
        self.assertContains(response, 'Internet')
        self.assertContains(response, 'Pending')