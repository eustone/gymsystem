


class GymManager:
    def __init__(self):
        self.customers = dict()
        self.packages = dict()
        self.subscriptions = dict()
        self.payments = dict()

    
    def add_customer(self, customer):
        self.customers[customer.get_customer_id()] = customer
