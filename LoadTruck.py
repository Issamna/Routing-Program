import csv

from HashTable import HashTable
from Location import Location
from Package import Package
from Truck import Truck

truck_1 = Truck(1)
truck_2 = Truck(2)

truck_3 = Truck(3)
must_go_with_truck1 = set()
not_sorted_packages = set()
location_hashtable = HashTable(27)
package_hashtable = HashTable(40)
truck_hashtable = HashTable(3)


# Load location data to hashtable: Space-Time Complexity = O(N)
def load_location_data():
    with open('LocationsData.csv', 'r') as csv_file:
        read_file = csv.reader(csv_file, delimiter=',')
        for row in read_file:
            location_id = row[0]
            location_name = row[1]
            location_address = row[2]
            location_city = row[3]
            location_state = row[4]
            location_zip = row[5]
            location_to_add = Location(location_id, location_name, location_address, location_city, location_state,
                                       location_zip)
            location_hashtable.put(location_id, location_to_add)


def add_to_truck(package_to_sort_id):
    package_to_sort = package_hashtable.get(package_to_sort_id)
    # if package is not urgent or is EOD
    if package_to_sort.deadline != 'EOD':
        # if package is not delayed
        if 'Delayed' not in package_to_sort.special:
            truck_1.add_package(int(package_to_sort_id), int(package_to_sort.location_id))
            # if the special note request it has to be delivered with another package, this adds to another set to keep
            # track. As these packages might not exist in the hashtable yet and cause run time error. Will be added in
            # during optimize phase
            if 'Delivered with' in package_to_sort.special:
                delivery_with_note = package_to_sort.special.split(",")
                must_go_with_truck1.add(int(delivery_with_note[1]))
                must_go_with_truck1.add(int(delivery_with_note[2]))

        else:
            truck_2.add_package(int(package_to_sort_id), int(package_to_sort.location_id))
    else:
        if 'Truck' in package_to_sort.special:
            truck_2.add_package(int(package_to_sort_id), int(package_to_sort.location_id))

        else:
            if int(package_to_sort_id) not in truck_1.truck_packages and int(
                    package_to_sort_id) not in truck_2.truck_packages and int(package_to_sort_id) not in must_go_with_truck1:
                not_sorted_packages.add(int(package_to_sort_id))


def get_location_id(package_id):
    package_found = package_hashtable.get(package_id)
    return int(package_found.location_id)


# Load location data to hashtable: Space-Time Complexity = O(N)
def load_package_data():
    with open('PackageData.csv', 'r') as csv_file:
        read_file = csv.reader(csv_file, delimiter=',')
        for row in read_file:
            package_id = row[0]
            package_location_id = row[1]
            package_deadline = row[6]
            package_weight = row[7]
            package_special = row[8]
            package_status = "AT HUB"
            package_to_add = Package(package_id, package_location_id, package_deadline, package_weight, package_special,
                                     package_status)
            package_hashtable.put(package_id, package_to_add)
            add_to_truck(package_id)


def load_trucks(not_sorted_packages):
    load_location_data()
    load_package_data()
    # Sub optimize the rest of the packages into the three trucks
    # Add in must_go_with_truck1 set to truck 1. Package_hashtable consists of all packages now
    for element_id in must_go_with_truck1:
        package_to_sort = package_hashtable.get(element_id)
        truck_1.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))

    # Iterate through the not sorted and add packages with similar address should be added to truck one and truck two
    for element_id in not_sorted_packages:
        package_to_sort = package_hashtable.get(element_id)
        if int(package_to_sort.location_id) in truck_1.truck_locations:
            if not truck_1.is_full() and 'Delayed' not in package_to_sort.special:
                truck_1.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
                not_sorted_packages = not_sorted_packages - truck_1.truck_packages
        if int(package_to_sort.package_id) not in truck_1.truck_packages and int(
                package_to_sort.location_id) in truck_2.truck_locations:
            if not truck_2.is_full() and 'Delayed - 10:20 am' not in package_to_sort.special:
                truck_2.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
                not_sorted_packages = not_sorted_packages - truck_2.truck_packages

    # sort not_sorted_packages by location id, so packages with similar destination are packed together
    not_sorted_packages = sorted(not_sorted_packages, key=get_location_id)

    # add the rest to truck 2 and truck 3
    for element_id in not_sorted_packages:
        package_to_sort = package_hashtable.get(element_id)
        if not truck_2.is_full() and 'Delayed - 10:20 am' not in package_to_sort.special:
            truck_2.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
        else:
            truck_3.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))

    # put trucks in hashtable for ease of access
    truck_hashtable.put(1, truck_1)
    truck_hashtable.put(2, truck_2)
    truck_hashtable.put(3, truck_3)



load_trucks(not_sorted_packages)

# print(len(not_sorted_packages))
# print(not_sorted_packages)
# print()
# print(len(truck_1.truck_packages))

# print()
# print(len(truck_2.truck_packages))
# print("Truck 2 packages: ")
# print(sorted(truck_2.truck_packages))
# print("Truck 2 locations: ")
# print(truck_2.truck_locations)
# print()
# print(len(truck_3.truck_packages))
# print("Truck 3 packages: ")
# print(sorted(truck_3.truck_packages))
# print("Truck 3 locations: ")
# print(truck_3.truck_locations)
