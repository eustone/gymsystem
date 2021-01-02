from idgenerator import CustomerID

class Customer:
    """
    Customer entity class.
    Private Attributes:
        customerID String
        name String
        phoneNo String
        joiningDate Date

    Public methods:
        Getters and setters
    """
    def __init__(self,name:str,
                phone_no:int,joined_date:str):
        self._name = name
        self._phone_no = phone_no
        self._joined_date = joined_date
        self._customer_id = CustomerID.customer_id()


    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self,name):
        self._name = name 

    
    @property
    def get_phone_no(self):
        return self._phone_no 

    @get_phone_no.setter
    def set_phone_no(self,phone_no):
        self._phone_no = phone_no

    @property
    def get_joined_date(self):
        return self._joined_date 

    @get_joined_date.setter
    def set_joined_date(self,joined_date):
        self._joined_date = joined_date

    @property
    def get_customer_id(self):
        return self._customer_id

    def __str__(self):
        return f"{self.get_name} {self.get_phone_no}{self.get_joined_date} {self.get_customer_id}"