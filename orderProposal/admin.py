from django.contrib import admin
from .models import OrderRequest, DeviceData, SensorData

admin.site.register(OrderRequest)
admin.site.register(DeviceData)
admin.site.register(SensorData)