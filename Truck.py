# Package object that stores Package information
# All methods space-time complexity is O(1) //for now


class Truck:

    # Constructor
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.start_time = start_time
        self.max_capacity = 16
        self.truck_packages = set()
        self.truck_locations = set()
        self.route = []
        self.distance = 0

    def print_contents(self):
        for i in self.truck_packages:
            print(self.truck_packages[i])

    def is_full(self):
        if len(self.truck_packages) >= self.max_capacity:
            return True
        else:
            return False

    def add_package(self, package_id, location_id):
        if self.is_full():
            print('truck full')
        else:
            self.truck_packages.add(package_id)
            self.truck_locations.add(location_id)

    def remove_package(self, package_id):
        if self.current_capacity <= 0:
            print('truck is empty')
            return False
        else:
            self.truck_packages.remove(package_id)
            return True
