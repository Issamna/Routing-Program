# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020


# Location object that stores location information
class Location:
    # Constructor
    # Complexity: O(1)
    def __init__(self, location_id: int, name, street, city, state, zip_code):
        self.location_id = location_id
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

