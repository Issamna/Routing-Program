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
        self.truck_packages = []
        self.truck_locations = []
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
    # Checks for repeats with 'in' = O(N)
    # Complexity: O(N)
    def add_package(self, package_id, location_id):
        if self.is_full():
            print('truck full')
        else:
            if package_id not in self.truck_packages:
                self.truck_packages.append(package_id)
            if location_id not in self.truck_locations:
                self.truck_locations.append(location_id)
