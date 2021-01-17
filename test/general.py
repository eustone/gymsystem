from random import randint
class TestDict:
    def __init__(self):
        self.cus_id = randint(100,2200)
        self.pac_id = randint(1,100)
        self.customers = dict()
        self.payments = dict()

    def add_customer(self,customer, amount):
        self.customers[customer] = customer
        self.payments[self.cus_id][self.pac_id] += amount