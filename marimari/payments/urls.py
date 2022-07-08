from django.urls import path
from .views import *

urlpatterns = [
  path('registerurl/',register_url, name="registerurl"),
  path('expresspay/',express_pay, name="expresspay"),
  path('confirmation/',mpesa_confirmation, name="confirmation"),
  path('validation/',mpesa_validation, name="validation"),
  path('expresspay_proccessor/',expresspay_proccessor, name="expresspay_proccessor"),
]