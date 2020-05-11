# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020

import csv
import math
from LoadTruck import truck_hashtable


# Method to get distance between two locations
# Complexity: O(1)
def get_distance(first_location_id, second_location_id):
    # Check if the locations are the same
    if first_location_id == second_location_id:
        return 0.0
    else:
        # Open data file
        with open('DistanceData.csv') as csv_file:
            distances_list = list(csv.reader(csv_file, delimiter=','))
            distance = distances_list[first_location_id][second_location_id]
            # If distance is '' flip the locations ids
            if distance == '':
                distance = distances_list[second_location_id][first_location_id]
        return float(distance)


# Method to grab the next closest location. Uses a greedy algorithm similar to shortest process next
# Compares the distance between start and a list of locations, returns the shortest one
# Complexity: O(N)
def next_location(start, locations):
    # If list is empty
    if len(locations) == 0:
        next = 0
        next_distance = get_distance(start, 0)
        return next, next_distance
    else:
        # Assumes the first location in list is the shortest distance
        next = locations[0]
        next_distance = get_distance(start, locations[0])
        # Iterates through list to and updates the next shortest distance
        for i in locations:
            if get_distance(start, i) < next_distance:
                next = i
                next_distance = get_distance(start, i)
        return next, next_distance


# Method to optimize a trucks route using a self-adjusting greedy algorithm (next_location method).
# Gets the trucks locations and then starting from the Hub (0) checks the next shortest path,
# which is added to a Route list. This algorithm ignores the packages and only deals with the
# locations. It chooses a suboptimal route for whatever the trucks locations are. It uses a while loop with
# a nested for loop, therefore having a complexity of O(N^2)
# Complexity: O(N^2)
def route_optimize(truck_num):
    # Get truck locations
    truck_locations = list(truck_hashtable.get(truck_num).truck_locations)
    total_distance = 0
    route = []
    current_location_id = 0
    # iterate through trucks locations
    while len(truck_locations) != 0:
        # Get next shortest location and distance
        next_location_id, distance_to_travel = next_location(current_location_id, truck_locations)
        # Add the next location to route list
        route.append(next_location_id)
        # Remove it from the list so it won't be used again, as it already has been visited
        truck_locations.remove(next_location_id)
        # Add the distance to total travelled distance
        total_distance = total_distance + distance_to_travel
        # Change current location to the next location and run loop again
        current_location_id = next_location_id
    # Once it reached its last location, return to hub: add that to list and add that distance
    route.append(0)
    total_distance = total_distance + get_distance(current_location_id, 0)
    # Update truck with the new optimized route and distance. I opted to round up instead of rounding to the nearest
    truck_hashtable.get(truck_num).route = route
    truck_hashtable.get(truck_num).distance = math.ceil(total_distance)


