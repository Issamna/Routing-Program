# Package object that stores Package information
# All methods space-time complexity is O(1) //for now
from typing import Any, Union


class Truck:

    # Constructor
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.current_capacity = 0
        self.max_capacity = 16
        self.truck_packages = set()
        self.distance = 0

    def print_contents(self):
        for i in self.truck_packages:
            print(self.truck_packages[i])

    def add_package(self, package_id):
        if self.current_capacity >= self.max_capacity:
            print('truck full')
            return False
        else:
            self.truck_packages.add(package_id)
            self.current_capacity =+ 1
            return True

    def remove_package(self, package_id):
        if self.current_capacity <= 0:
            print('truck is empty')
            return False
        else:
            self.truck_packages.remove(package_id)
            return True
