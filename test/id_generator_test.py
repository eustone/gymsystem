from uuid import uuid4
from idgenerator import PackageID,CustomerID


class TestCase():
    def test_package_id_generator():
        return PackageID.package_id().upper()


def generate_id():
    return uuid4().hex[:8]







print(test_package_id_generator())

