from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models import F, Sum
import datetime



class Category(models.Model):
    category_name = models.CharField(max_length=50 , null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name


class Seller(User):
    business_name = models.CharField(max_length=50)
    business_reg_no = models.CharField(max_length=50, blank=True)
    phone_number = models.IntegerField()
    external_url = models.CharField(max_length=100, blank=True)
    image_url = models.ImageField(upload_to='media/', blank=True, null=True)
    class Meta:
        verbose_name = "Seller"
    
    def __str__(self):
        return self.business_name


class Customer(User):
    phone_number = models.IntegerField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    OTP = models.IntegerField(null=True,blank=True)
    coupon_points = models.IntegerField(null=True,blank=True)
    device = models.CharField(max_length=200,blank=True,null=True)
    # REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Customer"

    def __str__(self):
        return self.username


class Product(models.Model):
    product_name = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    product_cost = models.FloatField( null=True, blank=True )
    inventory = models.IntegerField( null=True, blank=True)
    discounts = models.FloatField( null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,null=True, blank=True)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)
    user_cart = models.ManyToManyField(User, related_name="user_cart", blank=True) 
  

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    image1 = models.ImageField(upload_to='media/', blank=True, null=True)
    image2 = models.ImageField(upload_to='media/', blank=True, null=True)
    image3 = models.ImageField(upload_to='media/', blank=True, null=True)
    image4 = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.product.product_name

class County(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Counties"

    def __str__(self):
        return self.name
    
class DeliveryLocation(models.Model):
    name = models.CharField(max_length=50)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return     
    
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True) 
    delivery_location = models.ForeignKey(DeliveryLocation, on_delete=models.CASCADE, blank=True) 
    
    class Meta:
        verbose_name_plural= "Customer Adress"
    
    def __str__(self):
        return self.delivery_locationation
class Order(models.Model):
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today, null=True)
    status = models.BooleanField(default=False)
  
    def placeOrder(self):
        self.save()
  
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=True) 
    quantity = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.customer

class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    
    
    def __str__(self):
        return self.customer




class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    Created_at = models.DateTimeField()
    Updated_at = models.DateTimeField()
    duration = models.CharField(max_length=100)
   
    
    
    def __str__(self):
        return self.product


class Shipment(models.Model):
    delivery_location = models.ForeignKey(DeliveryLocation, on_delete=models.CASCADE, blank=True)
    transport_fee = models.IntegerField(default = 0)
    
    
    def __str__(self):
        return self.transport_fee

class Payment(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    status = (('not paid'),
            ('payment complete'))
    
    
    def __str__(self):
        return
    
class ShipmentStatus(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,null=True, blank=True)
    status = (('packaging'),('In transit'),('Arrived'))
    
    class Meta:
        verbose_name_plural = "Shipment Status"
    def __str__(self):
        return self.status
    
class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_code= models.IntegerField()
    time_of_payment = models.IntegerField()
    phone_number = models.IntegerField()
    amount = models.IntegerField()
    
    
    def __str__(self):
        return self.transaction_code
   
