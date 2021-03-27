from orders.models import Customer


def createCustomer(user):
    Customer.objects.create(account=user)
    print("customer created")
