from orders.views import CustomerViewSet, OrderCreateandListView, OrderDetailsDeleteView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('customers/', CustomerViewSet, basename='customers')
urlcustomers = router.urls


urlsorder = [
    path('createlist/', OrderCreateandListView.as_view()),
    path('retrievedelete/', OrderDetailsDeleteView.as_view())
]
