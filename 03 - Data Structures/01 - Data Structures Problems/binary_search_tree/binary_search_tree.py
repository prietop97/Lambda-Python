import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
import random


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # current = self
        node = BinarySearchTree(value)

        # while current:
        #     if current.value > value and current.left:
        #         current = current.left
        #     elif current.value > value and current.left is None:
        #         current.left = node
        #         break
        #     elif current.value <= value and current.right:
        #         current = current.right
        #     elif current.value <= value and current.right is None:
        #         current.right = node
        #         break


        if self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = node
        elif self.value <= value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = node


        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # current = self
        # while current:
        #     if current.value == target:
        #         return True
        #     elif current.value > target:
        #         current = current.left
        #     elif current.value < target:
        #         current = current.right

        # return False
        
        
        if self.value > target and self.left:
            return self.left.contains(target)
        if self.value < target and self.right:
            return self.right.contains(target)
        if self.value == target:
            return True
        
        return False



    # Return the maximum value found in the tree
    def get_max(self):
        # current = self
        # while current.right:
        #     current = current.right

        # return current.value
        if not self.right:
            return self.value
        return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        return cb(self.value)
        queue = Queue()
        queue.enqueue(node)
        # current = self
        # queue = Queue()
        # queue.enqueue(current)

        # while queue.len() > 0:
        #     current = queue.dequeue()
        #     cb(current.value)
        #     if current.left:
        #         queue.enqueue(current.left)
        #     if current.right:
        #         queue.enqueue(current.right)





    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self,node):

        # def dft_in_order(node):
        #     if node.left is None and node.right is None:
        #         print(node.value)
        #         return

        #     if node.left is not None:
        #         dft_in_order(node.left)
        #     print(node.value)
        #     if node.right is not None:
        #         dft_in_order(node.right)
            
        # dft_in_order(self)

        if not self.left and not self.right:
            print(self.value)
            return
        
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            

        def bft_rec(queue):
            if queue.len() <= 0:
                return
            current = queue.dequeue()
            print(current.value)
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)
            return bft_rec(queue)
            
        bft_rec(queue)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)


        
        # def dft_rec(node):
        #     print(node.value)

        #     if node.left is None and node.right is None:
        #         return

        #     if node.left is not None:
        #         dft_rec(node.left)
        #     if node.right is not None:
        #         dft_rec(node.right)

        # return dft_rec(node)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if not node.left and not node.right:
            return

        if node.left:
            self.pre_order_dft(node.left)

        if node.right:
            self.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):        
        if not node.left and not node.right:
            print(node.value)
            return

        if node.left:
            self.post_order_dft(node.left)

        if node.right:
            self.post_order_dft(node.right)
            
        print(node.value)

