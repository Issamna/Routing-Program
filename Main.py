from LoadData import location_hashtable, package_hashtable

for i in range(package_hashtable.table_size):
    package_print = package_hashtable.get(i + 1)
    print(package_print.location_id)
