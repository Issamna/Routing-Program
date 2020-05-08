# Location object that stores location information
# All methods space-time complexity is O(1)


class Location:
    # Constructor
    def __init__(self, location_id: int, name, street, city, state, zip_code):
        self.location_id = location_id
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    # To String method to print information
    def to_string(self):
        print(self.street + " | " + self.city + " | " + self.state + " | " + self.zip_code)
