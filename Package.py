# Package object that stores Package information
# All methods space-time complexity is O(1)


class Package:
    # Constructor
    def __init__(self, package_id: int, location_id, deadline, weight, special, status):
        self.package_id = package_id
        self.location_id = location_id
        self.deadline = deadline
        self.weight = weight
        self.special = special
        self.status = status

    # To String method to print information
    def to_string(self):
        print(
            "| " + str(self.package_id) + " | " + self.location_id + " | " + self.deadline + " | " + self.weight + " | " + self.special + " | ")
