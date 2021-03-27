from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

UserAccount = get_user_model()


class Customer(models.Model):
    account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    customer_id = models.UUIDField(primary_key=True,
                                   default=uuid.uuid4(),
                                   unique=True,
                                   editable=False)
    phone_number = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.account.email + "---"+ str(self.customer_id)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.CharField(max_length=200, null=False, blank=False)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.item
