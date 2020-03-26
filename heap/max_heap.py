class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        res = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return res


        

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        def bubble_rec(index,parent): ## Just for practice, I believe iteration is easier to read and less space consuming
            if parent < 0:
                parent = 0

            if self.storage[index] > self.storage[parent]:
                self.storage[index],self.storage[parent] = self.storage[parent],self.storage[index]

            if parent == 0:
                return

            index = parent
            return bubble_rec(index,(index - 1) // 2)

        bubble_rec(index,(index - 1) // 2)


    def _sift_down(self, index):
        
        while True:
            max_index = len(self.storage) - 1
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2
            highest_child_index = left_child_index
    
            if right_child_index <= max_index and self.storage[right_child_index] >= self.storage[left_child_index]:
                highest_child_index = right_child_index

            if len(self.storage) <= highest_child_index:
                break 

            if self.storage[highest_child_index] < self.storage[index]:
                break

            else:
                self.storage[index],self.storage[highest_child_index] = self.storage[highest_child_index],self.storage[index]
                index = highest_child_index


        

# my_heap = Heap()
# my_heap.insert(2)
# my_heap.insert(6)
# my_heap.insert(2)
# my_heap.insert(6)
# my_heap.insert(9)
# my_heap.insert(2)
# my_heap.insert(1)
# my_heap.insert(17)
# print(my_heap.storage)