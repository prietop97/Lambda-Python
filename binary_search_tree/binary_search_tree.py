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
        node = BinarySearchTree(value)
        current = self
        prev = self
        while current:
            prev = current
            if value < current.value:
                current = current.left
            elif value >= current.value:
                current = current.right
            
        
        if prev.value > value:
            prev.left = node
        elif prev.value <= value:
            prev.right = node
        




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while current:
            if current.value == target:
                return True
            elif current.value > target:
                current = current.left
            elif current.value < target:
                current = current.right

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right

        return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def rec_childs(node,left,right):
            if node is None:
                return False

            if node.left is not None:
                rec_childs(left,left.left,left.right)
            if node.right is not None:
                rec_childs(right,right.left,right.right)

            return cb(node.value)

            if not left and not right:
                return None

        rec_childs(self,self.left,self.right)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        def dft_in_order(node):
            if node.left is None and node.right is None:
                print(node.value)
                return

            if node.left is not None:
                dft_in_order(node.left)
            print(node.value)
            if node.right is not None:
                dft_in_order(node.right)
            
        dft_in_order(self)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
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
        
        def dft_rec(node):
            print(node.value)

            if node.left is None and node.right is None:
                return

            if node.left is not None:
                dft_rec(node.left)
            if node.right is not None:
                dft_rec(node.right)

        return dft_rec(node)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        def dft_rec(node):
            print(node.value)

            if node.left is None and node.right is None:
                return

            if node.left is not None:
                dft_rec(node.left)
            if node.right is not None:
                dft_rec(node.right)

        return dft_rec(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        def dft_rec(node):
        
            if node.left is None and node.right is None:
                print(node.value)
                return

            if node.left is not None:
                dft_rec(node.left)

            if node.right is not None:
                dft_rec(node.right)
            
            print(node.value)

        return dft_rec(node)


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.post_order_dft(bst)