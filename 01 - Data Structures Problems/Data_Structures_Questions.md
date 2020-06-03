Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
o(1)

2. What is the runtime complexity of `dequeue`?
o(1)

3. What is the runtime complexity of `len`?
o(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
o(logn)
2. What is the runtime complexity of `contains`?
o(logn)
3. What is the runtime complexity of `get_max`? 
o(logn)

## Heap

1. What is the runtime complexity of `_bubble_up`?
o(logn)
2. What is the runtime complexity of `_sift_down`?
o(log(n))
3. What is the runtime complexity of `insert`?
o(1) -> Only inserting, no bubble up -> o(logn)
4. What is the runtime complexity of `delete`?
o(1) --> Only deleting, no sift down -> o(logn)
5. What is the runtime complexity of `get_max`?
Depends on what heap you have, if a max heap then o(1)
## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
o(1)
2. What is the runtime complexity of `ListNode.insert_before`?
o(1)
3. What is the runtime complexity of `ListNode.delete`?
o(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
o(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
o(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
o(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
o(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
o(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
o(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
o(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    array since it have to shift everything over, with linked list it's either o(1) if you have a reference of the node you want to delete or o(n) just like array splice, so if you plan on saving references in something like a queque stack or hashmap etc, deleting and inserting will be o(1) with linked lists, also the first item(head) and last(tail) are always o(1) and arrays only the removal or inserting of the last item is o(1)