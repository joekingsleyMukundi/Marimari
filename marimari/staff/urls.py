from django.urls import path
from .views import *



urlpatterns = [
    path('dashboard/', dashboard, name = "dashboard"),
    # path('signin/', signin,name = "signin"),
    # path('signout/', signout, name = "signout"),
    # path('customers/', customers ,name = "customers"),
    # path('customers/register/', registerCustomer ,name = "register-customer"),
]
