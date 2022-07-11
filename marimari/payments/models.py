from django.db import models
from staff.models import Customer,Product

# Create your models here.

class Invoices (models.Model):
  user = models.ForeignKey(Customer, on_delete=models.CASCADE)
  order_id = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  status =models.CharField(max_length=200, default='Pending payment')

  def __str__(self):
    return self.order_id
class Orders(models.Model):
  order_invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
  order_amount = models.FloatField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

class Payments(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.CASCADE)
  Invoices = models.OneToOneField(Invoices, on_delete=models.CASCADE)
  amount = models.FloatField()
  tansaction_code = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  phone_number = models.CharField(max_length=200)

