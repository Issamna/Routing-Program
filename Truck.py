# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020


# Truck object that stores truck information
class Truck:

    # Constructor

    # Complexity: O(1)
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.start_time = start_time
        self.max_capacity = 16
        self.truck_packages = set()
        self.truck_locations = set()
        self.route = []
        self.distance = 0

    # Method checks to see if truck is full. Compares truck_packages length against max_capacity
    # Complexity: O(1)
    def is_full(self):
        if len(self.truck_packages) >= self.max_capacity:
            return True
        else:
            return False

    # Method to add package details into
    def add_package(self, package_id, location_id):
        if self.is_full():
            print('truck full')
        else:
            self.truck_packages.add(package_id)
            self.truck_locations.add(location_id)

