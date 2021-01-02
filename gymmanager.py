


class GymManager:
    def __init__(self):
        self.customers = dict()
        self.packages = dict()
        self.subscriptions = dict()
        self.payments = dict()

    
    def add_customer(self, customer):
        self.customers[customer.get_customer_id()] = customer
        self.subscriptions[customer.get_customer_id()] = dict()
        self.payments[customer.get_customer_id()] = dict()


    def add_package(self,package):
        self.packages[package.get_package_id()] = package

    def add_subscription(self,customer,package,months):
        package_id = package.get_package_id()
        customer_id = customer.get_customer_id()
        self.subscriptions[customer_id][package_id] = months

    
