import pdb
from gymmanager import GymManager
from customer import Customer 
from package import Package 


gymManager = GymManager()

print("\n")
print("******Amazing Gym Management System******")
print("Hello Admin, Please select a ")

def menu():
    print("1. Add Customer")
    print("2. Add Package")
    print("3. Show all packages")
    print("4. Show all customers")
    print("5. Find customer by name")
    print("6. Add Subscription")
    print("7. Add Payment")
    print("8. Show this menu again")
    print()
    

menu()
while True:
    try:
        selection = int(input("Enter Choice: "))
        if selection == 1:
            name = str(input("Enter customer name: "))
            phone_no = str(input("Enter customer phone no: "))
            joined_date = str(input("Enter joined date:"))
            customer = Customer(name, phone_no, joined_date)
            gymManager.add_customer(customer)
        elif selection == 2:
            name = input("Enter Package Name- ")
            facilities = input("Enter Facilities- ")
            cost = input("Enter cost- ")
            package = Package(name,facilities,cost)
            gymManager.add_package(package)

        elif selection == 3:
            for pkgId in gymManager.packages.keys():
                package = gymManager.packages[pkgId]
                packageId = pkgId
                package_names = package.get_package_name
                facilities = package.get_facilities
                cost = package.get_cost
                print(str(packageId) + "\t" + package_names + "\t" \
                     + facilities + "\t" + '$'+ str(cost) )

        elif selection == 4:
            for cId in gymManager.customers.keys():
                customer = gymManager.customers[cId]
                customer_id = cId
                print(customer_id)
                customer_names = customer.get_name
                print(str(customer_id) + '\t' + customer_names) 
                



    except ValueError as e:
        print("Wrong Entry. Enter a number")