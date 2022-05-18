
from rest_framework import serializers,exceptions
from ..models import OrderRequest, DeviceData, SensorData

class DeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceData
        fields = ['model', 'amount']

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['type','amount']
    

class OrderSerializer(serializers.ModelSerializer):
    devices = DeviceDataSerializer(many=True)
    sensors = SensorDataSerializer(many=True)
    class Meta:
        model = OrderRequest
        fields = ['id','customer','organization','place','state','devices','sensors','created_at','updated_at','is_cancelled','is_rejected']
    
    def create(self,validated_data):
        request_user = self.context["request"].user
        if request_user.role != 3:
            raise exceptions.PermissionDenied('you are not allowed to create order')

        devices = validated_data.pop('devices')
        sensors = validated_data.pop('sensors')
        order = OrderRequest.objects.create(created_by=request_user, **validated_data)
        order.save()
        for device in devices:
            deviceInstance = DeviceData.objects.create(order=order,**device)
            deviceInstance.save()
        for sensor in sensors:
            sensorInstance = SensorData.objects.create(order=order,**sensor)
            sensorInstance.save()
        return order




# {
#   "customer": 2,
#   "organization": 1,
#   "place": 1,
#   "devices": [
#       {
#           "model":1,
#           "amount":2
#     },
#     {
#           "model":1,
#           "amount":2
#     }
#   ],
#   "sensor": [
#       {
#           "type":1,
#           "amount":2
#     },
#     {
#           "type":1,
#           "amount":2
#     }
#   ],
# }