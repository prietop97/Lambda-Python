class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self,capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.length = 0
        self.load_factor = self.length / self.capacity
        self.minimum = 8

    def __len__(self):
        return self.length


    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        h = 3313  # arbitrary large prime number to initialize

        for char in key:
        # hash(i) = hash(i-1) * 33 + str[i]
            h = ((h << 5) + h) + ord(char)

    #return int(long(h)%long(size))  # python 2.7 needs some overflow magic
        return h

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hashed = self.hash_index(key)
        entry = HashTableEntry(key,value)
        if self.storage[hashed] is None:
            self.storage[hashed] = entry
        else:
            current = self.storage[hashed]
            prev = self.storage[hashed]

            while current:
                if current.key == key:
                    current.value = value
                    return

                prev = current
                current = current.next
                

            prev.next = entry
        
        self.length += 1
        if self.length / self.capacity >= 0.8:
            self.resize(self.capacity * 2) 


    def delete(self, key):
        
        deleted = False
        hashed = self.hash_index(key)
        current = self.storage[hashed]
        if current.key == key:
            self.storage[hashed] = current.next
            deleted = True
        else:
            while current.next:
                if current.next.key == key:
                    current.next = current.next.next
                    deleted = True
                    break
                current = current.next
        
        if deleted:
            self.length -= 1
            if self.length / self.capacity < 0.2 and self.capacity // 2 > self.minimum:
                self.resize(self.capacity // 2)  

        

    def get(self, key):
        hashed = self.hash_index(key)
        current = self.storage[hashed]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self,v):
        old_storage = self.storage
        self.capacity = v
        self.storage = [None] * self.capacity
        self.length = 0
        for nodes in old_storage:
            current = nodes
            while current:
                self.put(current.key,current.value)
                current = current.next
        
        

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
