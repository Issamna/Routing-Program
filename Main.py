from Distances import route_optimize
from LoadTruck import truck_hashtable
route_optimize(1)
route_optimize(2)
route_optimize(3)
print("Truck 1 packages: ")
print(sorted(truck_hashtable.get(1).truck_packages))
print("Truck 1 locations: ")
print(truck_hashtable.get(1).truck_locations)
print("Truck 1 Route: ")
print(truck_hashtable.get(1).route)
print("Truck 1 Distance: ")
print(round(truck_hashtable.get(1).distance,2))

print("")

print("Truck 2 packages: ")
print(sorted(truck_hashtable.get(2).truck_packages))
print("Truck 2 locations: ")
print(truck_hashtable.get(2).truck_locations)
print("Truck 2 Route: ")
print(truck_hashtable.get(2).route)
print("Truck 2 Distance: ")
print(round(truck_hashtable.get(2).distance,2))

print("")

print("Truck 3 packages: ")
print(sorted(truck_hashtable.get(3).truck_packages))
print("Truck 3 locations: ")
print(truck_hashtable.get(3).truck_locations)
print("Truck 3 Route: ")
print(truck_hashtable.get(3).route)
print("Truck 3 Distance: ")
print(round(truck_hashtable.get(3).distance,2))


print(round(truck_hashtable.get(1).distance,2)+round(truck_hashtable.get(2).distance,2)+round(truck_hashtable.get(2).distance,2))