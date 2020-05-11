# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020

import re
from Distances import route_optimize
from LoadTruck import truck_hashtable, package_hashtable
from Simulation import print_packages
# Main program to run simulation and user interface


# Method checks if user input is for time format is correct and in range
# Complexity: O(1)
def time_input_check(input: str):
    regex = re.compile(r"(?P<hour>\d+):(?P<minute>\d\d)")
    matches = regex.search(input)
    if len(input) > 5:
        return False, input, matches
    if not matches:
        return False, input, matches
    hour = int(matches.group('hour'))
    minute = int(matches.group('minute'))
    if hour > 23 or hour < 0:
        return False, hour, minute
    if minute > 59 or minute < 0:
        return False, hour, minute
    return True, hour, minute


# Main method to start program and user interface.
# It starts the program and uses the route_optimize method (O(N^2))
# Complexity: O(N^2)
def main_interface():
    route_optimize(1)
    route_optimize(2)
    route_optimize(3)

    # Main Interface
    print("C950 - Performance Assessment")
    print("Issam Ahmed         000846138")
    print("\n---------------------------------")
    print("WGUPS Delivery Tracking System")
    print("---------------------------------")
    total_distance = truck_hashtable.get(1).distance + truck_hashtable.get(2).distance + truck_hashtable.get(3).distance
    print("Truck 1 traveled distance: %d miles" % truck_hashtable.get(1).distance)
    print("Truck 2 traveled distance: %d miles" % truck_hashtable.get(2).distance)
    print("Truck 3 traveled distance: %d miles" % truck_hashtable.get(3).distance)
    print("Total traveled distance: %d miles" % total_distance)
    program_run = True
    # Run menu until exit is chosen
    # Checks for incorrect input and returns to menu
    while program_run:
        print("---------------------------------")
        print("             Menu                ")
        print("---------------------------------")
        print("1) Print all package by time")
        print("2) Print a package details by time")
        print("3) Print a package details by EOD")
        print("4) End of day delivery report")
        print("5) Exit")
        choice = input("Choose by number: ")
        if choice == '1':
            time_input = input("Enter Time between 00:00 and 23:59 in HH:MM format: ")
            is_input_correct, hour_input, minute_input = time_input_check(time_input)
            if is_input_correct:
                print_packages('All', hour_input, minute_input)
            else:
                print("Incorrect time format")
        elif choice == '2':
            time_input = input("Enter Time between 00:00 and 23:59 in HH:MM format: ")
            is_input_correct, hour_input, minute_input = time_input_check(time_input)
            if is_input_correct:
                try:
                    package_id_input = input("Enter package ID: ")
                    if int(package_id_input) < 1 or int(package_id_input) > package_hashtable.table_size:
                        print("Incorrect Package ID")
                    else:
                        print_packages(package_id_input, hour_input, minute_input)
                except ValueError:
                    print("Please enter an integer")
            else:
                print("Incorrect time format")
        elif choice == '3':
            try:
                package_id_input = input("Enter package ID: ")
                if int(package_id_input) < 1 or int(package_id_input) > package_hashtable.table_size:
                    print("Incorrect Package ID")
                else:
                    print_packages(package_id_input, 18, 0)
            except ValueError:
                print("Please enter an integer")
        elif choice == '4':
            print_packages('EOD', 18, 0)
        elif choice == '5':
            print("Exiting Program")
            program_run = False
        else:
            print("Wrong input")



# Run main interface
main_interface()

