"""
------------------------------------------------------------------------------------
Module Name: transformation_operations
------------------------------------------------------------------------------------

This module defines structural transformation operations for a doubly linked
list (DLL).

These operations modify the arrangement of nodes without changing the data
stored inside them. All transformations are performed at the link (pointer)
level.

Available functions:
- reverse_list
- rotate_list
- split_list
- merge_lists

All functions expect the doubly linked list (dll) to be passed explicitly as
the first argument unless otherwise stated.
------------------------------------------------------------------------------------
"""
from typing import Any

def reverse_list(dll):
    """
    Reverse the order of nodes in the doubly linked list.

    After this operation:
    - the head becomes the tail
    - the tail becomes the head
    - all next and prev links are reversed

    :param dll: Doubly linked list object
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Reverse Failed: the linked list is empty.")

    if dll.head == dll.tail:
        raise ValueError("Reverse Failed: Only one node in linked list")

    curr_node = dll.head
    old_head = dll.head
    old_tail = dll.tail

    while curr_node:
        # tuple atomic way - no need for temp variable
        # curr_node.prev, curr_node.next = curr_node.next, curr_node.prev
        temp = curr_node.prev
        curr_node.prev = curr_node.next
        curr_node.next = temp

        curr_node = curr_node.prev

    dll.head = old_tail
    dll.tail = old_head

    dll.head.prev = None
    dll.tail.next = None
    dll.print_linked_list()

def rotate_list(dll, k):
    """
    Rotate the doubly linked list by k positions.

    A positive k rotates the list to the right.
    A negative k rotates the list to the left.

    Rotation preserves node order cyclically and does not create or destroy
    nodes.

    :param dll: Doubly linked list object
    :param k: Number of positions to rotate
    :return: None
    """
    # STEP 1: identify rotation direction
    length = 0
    curr_node = dll.head
    while curr_node:
        length += 1
        curr_node = curr_node.next

    # STEP 2: normalize k
    # ex: length = 5 and k is 12 then 12 % 5 = 2,
    # first 10 rotations are full cycle rotation
    # we need to worry about last 2 rotations (rotate 1 node a time)

    knorm = abs(k) % length # rotate by this much
    if knorm == 0:
        print("No rotation required.")
        return
    if k > 0:
        direction = 'right'
        # when rotating by right, we need to identify split from end to head
        # that is why we need length - knorm
        # subtract one to use 0 based index
        split_node_index = length - knorm - 1
        print(
            f"Rotating list by right {abs(k)} times: "
            f"k = {abs(k)}, length = {length}, "
            f"knorm = {knorm}, split_node_index = {split_node_index}"
        )
    if k < 0:
        direction = 'left'
        # subtract one to use 0 based index
        split_node_index = knorm - 1
        print(
            f"Rotating list by left {abs(k)} times: "
            f"k = {abs(k)}, length = {length}, "
            f"knorm = {knorm}, split_node_index = {split_node_index}"
        )

    # STEP 3: Split list at split node index
    curr_node = dll.head
    while curr_node and split_node_index > 0:
        curr_node = curr_node.next
        split_node_index -= 1

    # split left and right sublist at curr node
    left_head, right_tail = dll.head, dll.tail

    # right sublist
    right_head = curr_node.next
    right_head.prev, right_tail.next = None, None

    # left sublist
    left_tail = curr_node
    left_head.prev, left_tail.next = None, None

    # STEP 4: perform rotation
    # merge -> append right_list to the head of left_list
    right_tail.next = left_head
    left_head.prev = right_tail

    # update head and tail & pointers for merged list
    dll.head, dll.tail = right_head, left_tail
    dll.head.prev, dll.tail.next = None, None

def split_list(dll, index, new_dll) -> (Any, Any):
    """
    Split the doubly linked list into two lists at the given position.

    The original list is divided such that:
    - the first list contains nodes up to the given position
    - the second list contains the remaining nodes

    Both resulting lists are independent and structurally valid.

    :param dll: Doubly linked list object
    :param index: Index at which to split the list
    :param new_dll: Doubly linked list object for second part
    :return: Tuple of two doubly linked list objects
    """
    if dll.is_empty():
        raise ValueError("Split Failed: the linked list is empty.")

    index = 0 if index == 0 else index - 1
    target_node = dll.search_by_index(index)

    if target_node is None:
        raise IndexError("Search By Index Failed: index is invalid.")
    if target_node == dll.head:
        return None, dll.head
    if target_node == dll.tail:
        return dll.head, None

    # split left and right sublist at curr node
    left_head, right_tail = dll.head, dll.tail

    # right sublist
    right_head = target_node.next
    right_head.prev, right_tail.next = None, None

    # left sublist
    left_tail = target_node
    left_head.prev, left_tail.next = None, None

    # return linked list objects
    dll.head, dll.tail = left_head, left_tail
    new_dll.head, new_dll.tail = right_head, right_tail

    return dll, new_dll

def merge_lists(dll1, dll2, mode):
    """
    Merge two doubly linked lists into a single list.

    The merge operation may be defined as:
    - appending dll2 to the end of dll1, or
    - interleaving nodes from both lists

    Both input lists must be structurally valid prior to merging.

    :param dll1: First doubly linked list
    :param dll2: Second doubly linked list
    :param mode: [append or alternate]
    :return: A new merged doubly linked list
    """
    if dll1.is_empty():
        dll1.head, dll1.tail = dll2.head, dll2.tail
        dll2.head = dll2.tail = None
        return dll1

    if dll2.is_empty():
        return dll1

    if mode == 'append':
        dll1.tail.next = dll2.head
        dll2.head.prev = dll1

        dll1.head, dll1.tail = dll1.head, dll2.tail
        dll1.head_prev, dll1.tail.next = None, None

        return dll1

    if mode == 'alternate':
        curr1, curr2 = dll1.head, dll2.head
        while curr1 and curr2:
            next1, next2 = curr1.next, curr2.next

            # insert curr2 after curr1
            curr1.next = curr2
            curr2.prev = curr1

            # reconnect next1 after curr2
            if next1:
                curr2.next = next1
                next1.prev = curr2
            else:
                dll1.tail = curr2
                curr2.next = None

            # advance pointers
            curr1, curr2 = next1, next2

        # if dll2 still has remaining nodes, append them
        if curr2:
            dll1.tail.next = curr2
            curr2.prev = dll1.tail
            dll1.tail = dll2.tail

        # empty dll2
        dll2.head = dll2.tail = None

        return dll1
    return None
