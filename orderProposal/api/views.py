from rest_framework import generics, viewsets , exceptions, response
from ..models import OrderRequest
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from utils.permissions import UserIsSystemInstaller

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset=OrderRequest.objects.all()
    permission_classes=[IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.role==2:
            self.queryset = OrderRequest.objects.filter(organization=user.organization)
        elif user.role==3:
            self.queryset = OrderRequest.objects.filter(created_by=user)
        return super().list(request, *args, **kwargs)


@api_view(['POST'])
@permission_classes([IsAuthenticated,UserIsSystemInstaller])
def CancelOrderViewSet(request,id):
    order = OrderRequest.objects.filter(id=id, created_by=request.user)
    if not order:
        raise exceptions.NotFound({"error":"order does not exist."})
    order=order[0]
    if order.is_cancelled:
        raise exceptions.ValidationError({"error":"order already cancelled."})

    order.is_cancelled=True
    order.save()
    return response.Response({"message":"Your order is successfully cancelled."})