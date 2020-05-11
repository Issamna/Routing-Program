# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020

import csv
from HashTable import HashTable
from Location import Location
from Package import Package
from Truck import Truck

# Load truck according to the requirements
# Truck 1 starting time is 8AM so 480 minutes
truck_1 = Truck(1, 480)
# Truck 2 starting time is 8AM so 545 minutes
truck_2 = Truck(2, 545)
# Truck 3 starting time is 8AM so 620 minutes
truck_3 = Truck(3, 620)
# List of packages that need to be added to truck 1 "Deliver with"
must_go_with_truck1 = list()
not_sorted_packages = list()
# Create hash tables for objects. Complexity: O(N)
location_hashtable = HashTable(27)
package_hashtable = HashTable(40)
truck_hashtable = HashTable(3)


# Load location data to hashtable
# Complexity: O(N)
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


# Method to check which truck package goes into.
# Complexity: O(N)
def add_to_truck(package_to_sort_id):
    # get package data from hashtable
    package_to_sort = package_hashtable.get(package_to_sort_id)
    # if package is not urgent or is EOD
    if package_to_sort.deadline != 'EOD':
        # if package is not delayed
        if 'Delayed' not in package_to_sort.special:
            truck_1.add_package(int(package_to_sort_id), int(package_to_sort.location_id))
            package_hashtable.get(package_to_sort_id).in_truck_num = 1
            # if the special note request it has to be delivered with another package, this adds to another list to keep
            # track. As these packages might not exist in the hashtable yet and cause run time error. Will be added in
            # during optimize phase
            if 'Delivered with' in package_to_sort.special:
                delivery_with_note = package_to_sort.special.split(",")
                if int(delivery_with_note[1]) not in must_go_with_truck1:
                    must_go_with_truck1.append(int(delivery_with_note[1]))
                if int(delivery_with_note[2]) not in must_go_with_truck1:
                    must_go_with_truck1.append(int(delivery_with_note[2]))
        # If package delayed and a priority out in truck 2
        else:
            truck_2.add_package(int(package_to_sort_id), int(package_to_sort.location_id))
            package_hashtable.get(package_to_sort_id).in_truck_num = 2
    else:
        # If it must be in truck 2
        if 'Truck' in package_to_sort.special:
            truck_2.add_package(int(package_to_sort_id), int(package_to_sort.location_id))
            package_hashtable.get(package_to_sort_id).in_truck_num = 2
        # Else check if in truck 1 or truck 2 or must_go_with_truck1 list
        else:
            if int(package_to_sort_id) not in truck_1.truck_packages and int(
                    package_to_sort_id) not in truck_2.truck_packages and int(
                    package_to_sort_id) not in must_go_with_truck1:
                if int(package_to_sort_id) not in not_sorted_packages:
                    not_sorted_packages.append(int(package_to_sort_id))


# Method get location id of package
# Complexity: O(1)
def get_location_id(package_id):
    package_found = package_hashtable.get(package_id)
    return int(package_found.location_id)


# Load location data to hashtable
# Add package to truck 1 or 2 depending on priority
# Complexity: O(N)
def load_package_data():
    with open('PackageData.csv', 'r') as csv_file:
        read_file = csv.reader(csv_file, delimiter=',')
        for row in read_file:
            package_id = row[0]
            package_location_id = row[1]
            package_deadline = row[6]
            package_weight = row[7]
            package_special = row[8]
            # Starting status is at Hub
            package_status = "AT HUB"
            package_to_add = Package(package_id, package_location_id, package_deadline, package_weight, package_special,
                                     package_status)
            package_hashtable.put(package_id, package_to_add)
            add_to_truck(package_id)


# Method loads location and package data, Loads truck
# Complexity: O(N^2)
def load_trucks(not_sorted_packages):
    load_location_data()
    load_package_data()
    # Sub optimize the rest of the packages into the three trucks
    # Add in must_go_with_truck1 list to truck 1. Package_hashtable consists of all packages now
    # Complexity: O(N)
    for element_id in must_go_with_truck1:
        package_to_sort = package_hashtable.get(element_id)
        truck_1.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
        package_hashtable.get(element_id).in_truck_num = 1

    # Iterate through the not sorted list and add packages with similar address in truck one and truck two
    # Uses a for loop (O(N)) and checks using a nested list 'in' method (O(N))
    # Complexity: O(N^2)
    for element_id in not_sorted_packages:
        package_to_sort = package_hashtable.get(element_id)
        # Check if the package location id is similar to the trucks 1 locations: Complexity: O(N)
        if int(package_to_sort.location_id) in truck_1.truck_locations:
            # If truck is not full or package is not delayed: Complexity: O(1)
            if not truck_1.is_full() and 'Delayed' not in package_to_sort.special:
                truck_1.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
                package_hashtable.get(element_id).in_truck_num = 1
                not_sorted_packages.remove(int(package_to_sort.package_id))
        # Check if the package location id is similar to the trucks 2 locations
        # and if not already in truck 1 : Complexity: O(N)
        if int(package_to_sort.package_id) not in truck_1.truck_packages and int(
                package_to_sort.location_id) in truck_2.truck_locations:
            # If truck is not full or package is not delayed: Complexity: O(1)
            if not truck_2.is_full() and 'Delayed - 10:20 am' not in package_to_sort.special:
                truck_2.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
                package_hashtable.get(element_id).in_truck_num = 2
                not_sorted_packages.remove(int(package_to_sort.package_id))

    # Sort not_sorted_packages by location id, so packages with similar destination are packed together
    # Complexity: O(N log N)
    not_sorted_packages = sorted(not_sorted_packages, key=get_location_id)

    # Add the rest to truck 2 and truck 3
    # Complexity: O(N)
    for element_id in not_sorted_packages:
        package_to_sort = package_hashtable.get(element_id)
        # If truck is not full or package is not delayed: Complexity: O(1)
        if not truck_2.is_full() and 'Delayed - 10:20 am' not in package_to_sort.special:
            truck_2.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
            package_hashtable.get(element_id).in_truck_num = 2
        else:
            truck_3.add_package(int(package_to_sort.package_id), int(package_to_sort.location_id))
            package_hashtable.get(element_id).in_truck_num = 3

    # Put trucks in hashtable for ease of access
    # Complexity: O(N)
    truck_hashtable.put(1, truck_1)
    truck_hashtable.put(2, truck_2)
    truck_hashtable.put(3, truck_3)

# Run load truck method
load_trucks(not_sorted_packages)

