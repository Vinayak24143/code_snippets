
from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()

from place.models import Place
from device.models import Category, SensorCategory
from organization.models import Organization



class OrderRequest(models.Model):

    ORDER_STATES = (
        (1, 'Placed'),
        (2, 'Accepted'),
        (3, 'Ready'),
        (4, 'Dispatched'),
        (5, 'Delivered'),
    )

    is_cancelled = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    customer = models.ForeignKey(User, limit_choices_to={"role":5},on_delete=models.CASCADE,related_name="customer")
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    state = models.PositiveSmallIntegerField(choices=ORDER_STATES, default=1)
    created_by = models.ForeignKey(User, limit_choices_to={"role":3}, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return "Order {} for {}".format(self.id, self.customer.email)

class DeviceData(models.Model):
    order = models.ForeignKey(OrderRequest, on_delete=models.CASCADE, related_name="devices")
    model = models.ForeignKey(Category, on_delete= models.CASCADE)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return str(self.model)

class SensorData(models.Model):
    order = models.ForeignKey(OrderRequest, on_delete=models.CASCADE, related_name="sensors")
    type = models.ForeignKey(SensorCategory, on_delete= models.CASCADE)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return str(self.type) 