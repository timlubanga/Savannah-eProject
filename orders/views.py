from orders.serializers import CustomerSerializer, OrderSerializer
from orders.models import Order, Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrderCreateandListView(generics.ListCreateAPIView):

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
