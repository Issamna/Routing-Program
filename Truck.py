# Package object that stores Package information
# All methods space-time complexity is O(1) //for now


class Truck:
    # Constructor
    def __init__(self, truck_id, current_capacity=0):
        self.truck_id = truck_id
        self.current_capacity = current_capacity
        self.max_capacity = 16

    def load(self):
        print("Truck " + self.truck_number + " loaded")
