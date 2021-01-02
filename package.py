from idgenerator import PackageID

class Package:
    def __init__(self, package_name, facilities, cost):
        self._package_name = package_name
        self._facilities = facilities
        self._cost = cost
        self._packageid = PackageID.package_id()

    @property
    def get_package_name(self):
        return self._package_name

    @get_package_name.setter
    def set_package_name(self,package_name):
        self._package_name = package_name

    @property
    def get_facilities(self):
        return self._facilities

    @get_facilities.setter
    def set_facilities(self,facilities):
        self._facilities = facilities

    @property
    def get_cost(self):
        return self._cost

    @get_cost.setter
    def set_cost(self,cost):
        self._cost = cost

    @property
    def get_package_id(self):
        return self._packageid

    def __str__(self):
        return f"{self.get_package_name()} {self.get_facilities()}" \
               f" {self.get_cost} {self.get_package_id}"
