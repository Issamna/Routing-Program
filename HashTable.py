# Hashtable


class HashTable:
    # Constructor: Time Complexity = O(1); Space Complexity = O(N)
    def __init__(self, table_size):
        self.table = [None] * table_size
        self.table_size = table_size

    # Returns hash value based on elements key: Time Complexity = O(1)
    def get_hash_index(self, key):
        return int(key) % self.table_size



    # Put element into hash table using key(new and update): Time Complexity = O(1)
    # Not expecting any collisions
    def put(self, key, element):
        index = int(self.get_hash_index(key))
        # if the index is empty
        if self.table[index] is None:
            self.table[index] = [key, element]
        # if not empty
        elif self.table[index][0] == key:
            # update element and return
            self.table[index][1] = element
        # Not expecting collisions, This is for error checking
        else:
            print("collision")

    # Search and return element corresponding to key: Time Complexity = O(1)
    def get(self, key: int):
        index = self.get_hash_index(key)
        if self.table[index] is None:
            return None
        else:
            return self.table[index][1]