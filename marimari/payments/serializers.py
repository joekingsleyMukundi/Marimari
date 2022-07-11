from rest_framework import serializers
from .models import *


class OrdersSerializers(serializers.ModelSerializer):
  class Meta:
        model = Orders
        fields = '__all__'