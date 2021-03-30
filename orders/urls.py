from orders.views import CustomerViewSet, OrderCreateandListView, OrderDetailsDeleteView, RetrieveandUpdateCustomerView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('', CustomerViewSet, basename='customers')
urlcustomers = router.urls


urlsorder = [
    path('createlist/', OrderCreateandListView.as_view(),
         name="createandlistorders"),
    path('retrievedelete/<int:pk>/', OrderDetailsDeleteView.as_view(),
         name="retrieveanddeleteorders")
]


urlscustomerupdate = [
    path('Me/', RetrieveandUpdateCustomerView.as_view(), name="customerDetails")]
