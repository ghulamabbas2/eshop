from dataclasses import field
from pyexpat import model
from django_filters import rest_framework as filters
from .models import Order

class OrdersFilter(filters.FilterSet):

    class Meta:
        model = Order
        fields= ('id', 'status', 'payment_status', 'payment_mode')