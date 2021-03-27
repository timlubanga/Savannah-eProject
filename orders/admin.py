from django.contrib import admin
from orders.models import Customer, Order

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_id", "phone_number", "account"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "item", "quantity"]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
