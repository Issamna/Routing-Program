# Package object that stores Package information
# All methods space-time complexity is O(1)


class Package:
    # Constructor
    def __int__(self, package_id, location, deadline, weight, special, status=None):
        self.package_id = package_id
        self.location = location
        self.deadline = deadline
        self.weight = weight
        self.special = special
        self.status = status

    # To String method to print information
    def to_string(self):
        print(
            "| " + self.package_id + " | " + self.location.to_string() + " | " + self.deadline + " | " + self.weight + " | " + self.special + " | ")
