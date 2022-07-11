from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *



class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('registerurl')
        self.assertEqual(resolve(url).func, register_url)

    def test_expresspay_is_resolved(self):
        url = reverse('user_profile')
        self.assertEqual(resolve(url).func, expresspay)

    def test_confirmation_url_is_resolved(self):
        url = reverse('confirmation')
        print(resolve(url).func)
        self.assertEqual(resolve(url).func, mpesa_confirmation)
    
    def test_validation_url_is_resolved(self):
        url = reverse('validation')
        self.assertEqual(resolve(url).func, mpesa_validation)
    def test_expresspay_proccessor_url_is_resolved(self):
        url = reverse('expresspay_proccessor')
        self.assertEqual(resolve(url).func, expresspay_proccessor)

# Create your tests here.
