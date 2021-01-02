from uuid import uuid4

class CustomerID:
    @staticmethod
    def customer_id():
        try:
            return uuid4().hex[:8].upper()
        except KeyError:
            raise("Customer ID not generated")   
        

class PackageID:
    @staticmethod
    def package_id():
        try:
            return uuid4().hex[:8].upper()
        except ValueError:
            raise("Package ID not generated")
        

   