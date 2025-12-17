"""
------------------------------------------------------------------------------------
Module Name: sort_operations
------------------------------------------------------------------------------------

This module defines sorting operations for a doubly linked list (DLL).

Sorting is performed by rearranging node links (prev / next pointers)
rather than copying data into auxiliary structures.

These operations assume the doubly linked list is structurally valid
before sorting begins.

Available functions:
- sort_ascending
- sort_descending

All functions expect the doubly linked list (dll) to be passed explicitly
as the first argument.
------------------------------------------------------------------------------------
"""
from typing import Any


def sort_ascending(dll) -> None:
    """
    Sort the doubly linked list in ascending order.

    The sorting operation rearranges nodes in-place by updating
    their prev and next pointers. No new nodes are created.

    Recommended approach:
    - Merge Sort (stable and optimal for linked lists)

    :param dll: Doubly linked list object
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Sort Failed: the linked list is empty.")

    if dll.head == dll.tail:
        return  # single node list is already sorted

    length = dll.get_length()

    for itr in range(0, length - 2):
        curr_node = dll.head
        while curr_node.next:
            if curr_node.data > curr_node.next.data:
                next_node = curr_node.next
                temp = curr_node.data
                curr_node.data = next_node.data
                next_node.data = temp

            curr_node = curr_node.next

def sort_descending(dll) -> None:
    """
    Sort the doubly linked list in descending order.

    This operation rearranges node links to produce a descending
    order of elements.

    Implementation options:
    - Perform ascending sort, then reverse the list
    - Implement comparator-based merge sort

    :param dll: Doubly linked list object
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Sort Failed: the linked list is empty.")

    if dll.head == dll.tail:
        return  # single node list is already sorted

    length = dll.get_length()

    for itr in range(0, length - 2):
        curr_node = dll.head
        while curr_node.next:
            if curr_node.data < curr_node.next.data:
                next_node = curr_node.next
                temp = curr_node.data
                curr_node.data = next_node.data
                next_node.data = temp

            curr_node = curr_node.next


