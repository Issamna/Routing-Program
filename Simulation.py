import math
from Distances import route_optimize, next_location, get_distance
from LoadTruck import package_hashtable, truck_hashtable, location_hashtable

route_optimize(1)
route_optimize(2)
route_optimize(3)


def time_minutes_format(hour: int, minute: int):
    time_in_minutes = (hour * 60) + minute
    return int(time_in_minutes)


def time_clock_format(time_in_minutes):
    hour = int(time_in_minutes / 60)
    minutes = time_in_minutes - (hour * 60)
    return hour, minutes


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
        print("Package ID: ", package_id, "Street :", street, "City: ", city, "ZIP: ", zip_code, "Deadline: ", deadline,
              "Weight: ", weight, "Delivery Status: ", status)


def run_truck(minutes, truck_id):
    start_time = truck_hashtable.get(truck_id).start_time
    if minutes < start_time:
        pass
    else:
        distance_travelled = (minutes - start_time) / 60 * 18
        truck_route = list(truck_hashtable.get(truck_id).route)
        current_distance = 0
        locations_visited = []
        time_to_locations = []
        current_location_id = 0
        while len(truck_route) != 0 and current_distance <= distance_travelled:
            distance_to_travel = get_distance(current_location_id, truck_route[0])
            current_distance = current_distance + distance_to_travel
            if current_distance <= distance_travelled:
                locations_visited.append((truck_route[0]))
                time_to_locations.append(math.ceil((current_distance / 18) * 60))
                current_location_id = truck_route[0]
                truck_route.remove(truck_route[0])
        for element_id in truck_hashtable.get(truck_id).truck_packages:
            if int(package_hashtable.get(element_id).location_id) in locations_visited:
                location_time = time_to_locations[
                    (locations_visited.index(int(package_hashtable.get(element_id).location_id)))]
                hour, minute = time_clock_format(location_time + start_time)
                package_hashtable.get(element_id).status = "Delivered at " + time_print_format(hour, minute)
            else:
                package_hashtable.get(element_id).status = "On Route"


def print_packages(package_id, hour, minute):
    time_in_minutes = time_minutes_format(hour, minute)
    run_truck(time_in_minutes, 1)
    run_truck(time_in_minutes, 2)
    run_truck(time_in_minutes, 3)
    if package_id == 'EOD' or package_id == 'All':
        all_packages_print()
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
        print("Package ID: ", package_id, "Street :", street, "City: ", city, "ZIP: ", zip_code, "Deadline: ", deadline,
              "Weight: ", weight, "Delivery Status: ", status)
