# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020


# Package object that stores package information
class Package:
    # Constructor
    # Complexity: O(1)
    def __init__(self, package_id: int, location_id, deadline, weight, special, status):
        self.package_id = package_id
        self.location_id = location_id
        self.deadline = deadline
        self.weight = weight
        self.special = special
        self.status = status
        self.in_truck_num = 0




