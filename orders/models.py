from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.sms import sendOrderSms
from orders.twillionSms import twilioSms


UserAccount = get_user_model()


class Customer(models.Model):
    account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    customer_id = models.UUIDField(primary_key=True,
                                   default=uuid.uuid4(),
                                   unique=True,
                                   editable=False)
    phone_number = models.CharField(
        max_length=300, null=True, blank=True, default="+254714568338")

    def __str__(self):
        return self.account.email


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.CharField(max_length=200, null=False, blank=False)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.item


@receiver(post_save, sender=Order)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.customer.phone_number:
            pass
            # twilioSms(instance)
