from uuid import uuid4
from idgenerator import PackageID




def generate_id():
    return uuid4().hex[:8]



def test_package_id_generator():
    return PackageID.package_id().upper()



print(test_package_id_generator())

