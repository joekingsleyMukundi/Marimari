from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(County)
admin.site.register(DeliveryLocation)
admin.site.register(Cart)
admin.site.register(Offer)
admin.site.register(Shipment)
admin.site.register(Payment)
admin.site.register(ShipmentStatus)
admin.site.register(Transaction)
admin.site.register(ProductImage)

