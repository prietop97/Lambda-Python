# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return 1

    def pop(self):
        if self.size == 0:
            return

        self.size -= 1
        return self.storage.pop()

    def len(self):
        return self.size
