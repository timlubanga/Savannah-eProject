import boto3


def sendmessagenotification(order):
    client = boto3.client("sns", "us-east-2")
    number = order.customer.phone_number

    client.publish(PhoneNumber=number,
                   Message='order with id{id} has been created successffully'.format(id=order.id))
