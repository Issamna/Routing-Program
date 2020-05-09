import csv
from LoadTruck import truck_hashtable


# get distance between two locations
def get_distance(first_location_id, second_location_id):
    if first_location_id == second_location_id:
        return 0.0
    else:
        with open('DistanceData.csv') as csv_file:
            distances_list = list(csv.reader(csv_file, delimiter=','))
            distance = distances_list[first_location_id][second_location_id]
            if distance == '':
                distance = distances_list[second_location_id][first_location_id]
        return float(distance)


def next_location(start, locations):
    if len(locations) == 0:
        next = 0
        next_distance = get_distance(start, 0)
        return next, next_distance
    else:
        next = locations[0]
        next_distance = get_distance(start, locations[0])
        for i in locations:
            if get_distance(start, i) < next_distance:
                next = i
                next_distance = get_distance(start, i)
        return next, next_distance


def route_optimize(truck_num):
    truck_locations = list(truck_hashtable.get(truck_num).truck_locations)
    total_distance = 0
    route = []
    current_location_id = 0
    while len(truck_locations) != 0:
        next_location_id, distance_to_travel = next_location(current_location_id, truck_locations)
        route.append(next_location_id)
        truck_locations.remove(next_location_id)
        # print("Current: "+str(current_location_id)+" Next: "+str(next_location_id)+" distance: "+str(distance_to_travel))
        total_distance = total_distance + distance_to_travel
        current_location_id = next_location_id
    route.append(0)
    total_distance = total_distance + get_distance(current_location_id, 0)
    truck_hashtable.get(truck_num).route = route
    truck_hashtable.get(truck_num).distance = total_distance
