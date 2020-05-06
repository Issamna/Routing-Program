# Hashtable


class HashTable:
    # Constructor: Time Complexity = O(1); Space Complexity = O(N)
    def __init__(self, table_size: int):
        self.table = [] * table_size

    # Returns hash value based on elements key: Time Complexity = O(1)
    def get_hash_index(self, key: int):
        return key % len(self.table)

    # Put element into hash table using key(new and update): Time Complexity = O(1)
    # Not expecting any collisions
    def put(self, key, element):
        index = self.get_hash_index(key)
        # if the index is empty
        if self.table[index] is None:
            self.table[index] = [key, element]
            return True
        # if not empty
        elif self.table[index][0] == key:
            # update element and return
            self.table[index][1] = element
            return True
        # Not expecting collisions, This is for error checking
        else:
            print("collision")
            return False

    # Search and return element corresponding to key: Time Complexity = O(1)
    def search(self, key: int):
        index = self.get_hash_index(key)
        if self.table[index] is None:
            return None
        else:
            return self.table[index][1]
