from orders.serializers import CustomerSerializer, OrderSerializer
from orders.models import Order, Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from drf_yasg import openapi

account = openapi.Parameter(
    "account", nullable=True, type=openapi.TYPE_OBJECT, in_=openapi.IN_BODY)


class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class RetrieveandUpdateCustomerView(generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_object_or_404(
            Customer, customer_id=request.user.customer.customer_id)
        serializer = CustomerSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_STRING, required="phone_number"))
    def patch(self, request):
        customer = request.user.customer
        data = request.data
        serializer = CustomerSerializer(customer, data=data, partial=True, context={
                                        "method": request.method})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class OrderCreateandListView(generics.GenericAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=request.user.customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = Order.objects.filter(customer=request.user.customer)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailsDeleteView(generics.RetrieveDestroyAPIView):

    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
