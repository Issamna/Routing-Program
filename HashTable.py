# C950 Performance Assessment
# Issam Ahmed
# 000846138
# 5/10/2020

# Hashtable for program
# Must be set with a size. Since the requirements have a predetermined number of packages, locations, trucks


class HashTable:
    # Constructor
    # Complexity: O(N)
    # Creates a list of nones
    def __init__(self, table_size):
        self.table = [None] * table_size
        self.table_size = table_size

    # Returns hash value based on elements key
    # Complexity: O(1)
    def get_hash_index(self, key):
        return int(key) % self.table_size

    # Put element into hash table using key(new and update)
    # Since this hashtable is already set with empty, it uses the index to
    # gets the key location and updates the element
    # Complexity: O(1)
    # Not expecting any collisions
    def put(self, key, element):
        index = int(self.get_hash_index(key))
        # if the index is empty/None
        if self.table[index] is None:
            self.table[index] = [key, element]
        # if not empty/None and equals the key
        elif self.table[index][0] == key:
            # update element and return
            self.table[index][1] = element
        # Not expecting collisions, This is for error checking
        else:
            print("collision")

    # Return element corresponding to key
    # Complexity: O(1)
    def get(self, key: int):
        index = self.get_hash_index(key)
        if self.table[index] is None:
            return None
        else:
            return self.table[index][1]
