from unicodedata import category
from django.urls import path
from .views import *


app_name = "categories"
  
  
urlpatterns = [
  path("category/<int:id>/",categoryNav, name="prods-category")
]