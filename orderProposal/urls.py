from django.urls import path
from orderProposal.api import views

urlpatterns=[
    path('', views.OrderViewSet.as_view({'get': 'list','post':'create'}), name='order'),
    path('cancel/<int:id>', views.CancelOrderViewSet, name="cancelOrder" ),
]