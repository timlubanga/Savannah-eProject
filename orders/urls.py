from orders.views import CustomerViewSet, OrderCreateandListView, OrderDetailsDeleteView, UpdateCustomerPhoneNumberView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('', CustomerViewSet, basename='customers')
urlcustomers = router.urls


urlsorder = [
    path('createlist/', OrderCreateandListView.as_view()),
    path('retrievedelete/', OrderDetailsDeleteView.as_view())
]


urlscustomerupdate = [
    path('Me/', UpdateCustomerPhoneNumberView.as_view())]
