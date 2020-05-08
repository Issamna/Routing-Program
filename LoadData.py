import csv

from HashTable import HashTable
from Location import Location
from Package import Package
from Truck import Truck

truck_1 = Truck(1)
truck_2 = Truck(2)
truck_3 = Truck(3)
not_sorted_packages = set()
# Load location data to hashtable: Space-Time Complexity = O(N)
with open('LocationsData.csv', 'r') as csv_file:
    read_file = csv.reader(csv_file, delimiter=',')
    location_hashtable = HashTable(27)
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
            truck_1.add_package(int(package_to_sort_id))

        else:
            truck_2.add_package(int(package_to_sort_id))
    else:
        if 'Truck' in package_to_sort.special:
            truck_2.add_package(int(package_to_sort_id))
        else:
            not_sorted_packages.add(int(package_to_sort_id))


# Load location data to hashtable: Space-Time Complexity = O(N)
with open('PackageData.csv', 'r') as csv_file:
    read_file = csv.reader(csv_file, delimiter=',')
    package_hashtable = HashTable(40)
    for row in read_file:
        package_id = row[0]
        package_location_id = row[1]
        package_deadline = row[6]
        package_weight = row[7]
        package_special = row[8]
        package_status = "AT HUB"
        package_to_add = Package(package_id, package_location_id, package_deadline, package_weight, package_special, package_status)
        package_hashtable.put(package_id, package_to_add)
        add_to_truck(package_id)


print(truck_1.truck_packages)
print(truck_2.truck_packages)
print(not_sorted_packages)




