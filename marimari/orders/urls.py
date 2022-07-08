from django.urls import path
from .views import *

app_name = "orders"

urlpatterns = [  
    path('cart/', cart,name = "cart"), 
    path('cart/add_to_cart/<int:id>', add_to_cart, name = "user_cart"),
    path('wishlist/', wishlist ,name = "wishlist"),
    path('wishlist/add_to_wishlist/<int:id>', add_to_wishlist,name = "user_wishlist"),
    # path("cart/quantity", cartQuantity ,name="quantity"),    
]