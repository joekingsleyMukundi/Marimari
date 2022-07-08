from django.urls import path
from .views import *
from logins import views
  
  
  
urlpatterns = [
    path('logins/about/', about,name = "about"),
    path('home/', home, name = "home"),
    path('logins/verify/', verification, name = "verify"),
    path('signout/', signout,name = "signout"),
    path('signin/', signin,name = "signin"),
    path('register/', register,name = "register"),    
]