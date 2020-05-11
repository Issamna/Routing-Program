# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020

# Simulation to run truck routes and see delivery information
import math
from Distances import get_distance
from LoadTruck import package_hashtable, truck_hashtable, location_hashtable


# Changes Hour(24hr clock) and minutes into total minutes
# Complexity: O(1)
def time_minutes_format(hour: int, minute: int):
    time_in_minutes = (hour * 60) + minute
    return int(time_in_minutes)


# Changes total minutes into how many hours and minutes
# Complexity: O(1)
def time_clock_format(time_in_minutes):
    hour = int(time_in_minutes / 60)
    minutes = time_in_minutes - (hour * 60)
    return hour, minutes


# Changes hours and minutes into a clock format
# Complexity: O(1)
def time_print_format(hour, minute):
    if len(str(hour)) == 2:
        hour_string = str(hour)
    else:
        hour_string = "0" + str(hour)
    if len(str(minute)) == 2:
        minute_string = str(minute)
    else:
        minute_string = "0" + str(minute)

    return hour_string + ":" + minute_string


# Gets all packages in the hash table and returns information to be printed
# Complexity: O(N)
def all_packages_print():
    for element_id in range(1, package_hashtable.table_size + 1):
        package = package_hashtable.get(element_id)
        location = location_hashtable.get(package.location_id)
        package_id = element_id
        street = location.street
        deadline = package.deadline
        city = location.city
        zip_code = location.zip_code
        weight = package.weight
        status = package.status
        print("|Package ID:", package_id, "| Street:", street, "| City:", city, "| ZIP:", zip_code, "| Deadline:",
              deadline,
              "| Weight:", weight, "| Delivery Status:", status)


# Method to reset status for new query
# Complexity: O(N)
def reset_all_packages_status():
    for element_id in range(1, package_hashtable.table_size + 1):
        package_hashtable.get(element_id).status = "At Hub"


# Method to run each truck in the simulation
# Complexity: O(N^2)
def run_truck(minutes, truck_id):
    # Start time to help with the offset of when truck leaves the Hub
    start_time = truck_hashtable.get(truck_id).start_time
    # If the less then the start time, the truck and its packages are still in the hub
    if minutes < start_time:
        pass
    else:
        # Calculate the distance the truck has travelled in those minutes if running at 18MPH
        distance_travelled = (minutes - start_time) / 60 * 18
        # Sets variables to be used
        truck_route = list(truck_hashtable.get(truck_id).route)
        current_distance = 0
        locations_visited = []
        time_to_locations = []
        current_location_id = 0
        # Iterates through the route list and while the current distance is less than the distance travelled
        # Complexity: O(N)
        while len(truck_route) != 0 and current_distance <= distance_travelled:
            # Get the distance travelled and add it to the distance count
            distance_to_travel = get_distance(current_location_id, truck_route[0])
            current_distance = current_distance + distance_to_travel
            # Checks if the distance is still less than the distance the truck will cover
            if current_distance <= distance_travelled:
                # Adds the location to a list of visited locations during the distance it covered in specified minutes
                locations_visited.append((truck_route[0]))
                # Adds the time it took corresponding to the locations truck visited
                time_to_locations.append(math.ceil((current_distance / 18) * 60))
                # change next route and remove current location from list
                current_location_id = truck_route[0]
                truck_route.remove(truck_route[0])
        # Locations visited and Packages delivered in the time frame is now updated with a timestamp
        # In the for loop it checks if the package location exists in locations_visited list therefore
        # Complexity is O(N^2)
        for element_id in truck_hashtable.get(truck_id).truck_packages:
            # If package location exists in location visited
            if int(package_hashtable.get(element_id).location_id) in locations_visited:
                # Get the corresponding time stamp
                location_time = time_to_locations[
                    (locations_visited.index(int(package_hashtable.get(element_id).location_id)))]
                hour, minute = time_clock_format(location_time + start_time)
                # Update the package's status
                package_hashtable.get(element_id).status = "Delivered at " + time_print_format(hour, minute)
            else:
                # Package still in route if not in locations_visited
                package_hashtable.get(element_id).status = "On Route"


# Prints package information at the given hour and minute
# Uses run_truck method, therefore
# Complexity: O(N^2)
def print_packages(package_id, hour, minute):
    # Changes hour and minute to total minutes
    time_in_minutes = time_minutes_format(hour, minute)
    # Run trucks
    run_truck(time_in_minutes, 1)
    run_truck(time_in_minutes, 2)
    run_truck(time_in_minutes, 3)
    # If requested information is all or EOD
    if package_id == 'EOD' or package_id == 'All':
        all_packages_print()
    # Prints individual package information requested
    else:
        package = package_hashtable.get(package_id)
        location = location_hashtable.get(package.location_id)
        package_id = package_id
        street = location.street
        deadline = package.deadline
        city = location.city
        zip_code = location.zip_code
        weight = package.weight
        status = package.status
        print("|Package ID:", package_id, "| Street:", street, "| City:", city, "| ZIP:", zip_code, "| Deadline:",
              deadline,
              "| Weight:", weight, "| Delivery Status:", status)
    # Reset package status for new query
    reset_all_packages_status()
