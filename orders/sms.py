import africastalking
import os


def sendOrderSms(order):
    # Initialize SDK
    username = os.environ.get("SMSSUSERNAME")
    # use your sandbox app API key for development in the test environment
    api_key = os.environ.get("SMSAPI_KEY")
    africastalking.initialize(username, api_key)

    sms = africastalking.SMS


# Use the service synchronously
    number = order.customer.phone_number
    response = sms.send(
        'order with id{id} has been created successffully'.format(id=order.id), [number])
    print(response)
