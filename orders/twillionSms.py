from twilio.rest import Client
import os


def twilioSms(order):
    account = os.environ.get("ACCOUNTSSID")
    token = os.environ.get("TWILLIOTOKEN")
    client = Client(account, token)
    number = order.customer.phone_number
    print(number)
    message = client.messages.create(to=number, from_="+14695572774",
                                     body="Dear {name} your order with an id of {id} has been successfully created".format(id=order.id, name=order.customer.account.email))
