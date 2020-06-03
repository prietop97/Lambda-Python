from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) != self.capacity:
            self.storage.add_to_tail(item)
            return

        if self.current is None:
            self.storage.head.value = item
            self.current = self.storage.head.next
            return
        
        self.current.value = item
        self.current = self.current.next

        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None for i in range(capacity)]

    def append(self, item):        
        if self.current == len(self.storage):
            self.current = 0

        self.storage[self.current] = item
        self.current += 1
        


    def get(self):
        storage = []
        
        for val in self.storage:
            if not val:
                break
            storage.append(val)

        return storage
