"""
------------------------------------------------------------------------------------
Module: Doubly Linked List Helper Utilities
------------------------------------------------------------------------------------
This module provides utility and helper functions for a doubly linked list.
These functions expose commonly required operations such as conversion,
introspection, and positional access without modifying list structure.
------------------------------------------------------------------------------------
Available Functions:
    - to_list(dll)
    - from_list(values)
    - get_length(dll)
    - get_middle_node(dll)
    - get_nth_from_start(dll, n)
    - get_nth_from_end(dll, n)
------------------------------------------------------------------------------------
"""

def to_list(dll) -> list:
    """
    Function: Convert the linked list to a Python list
    :param dll: Doubly linked list instance
    :return: List containing node values in order
    """
    dll_info = dll.traverse()
    values = dll_info['values']
    return values

def from_list(dll, values):
    """
    Function: Create a doubly linked list from a Python list
    :param dll: linked list object
    :param values: Iterable of values to populate the linked list
    :return: Doubly linked list instance
    """
    if not values:
        raise ValueError("From_List Failed: the values list is empty.")
    for value in values:
        dll.insert_at_tail(value)

def get_length(dll) -> int:
    """
    Function: Get the number of nodes in the linked list
    :param dll: Doubly linked list instance
    :return: Total number of nodes
    """
    dll_info = dll.traverse()
    return dll_info['length']

def get_middle_node(dll):
    """
    Function: Get the middle node of the linked list
    :param dll: Doubly linked list instance
    :return: Middle node if list is not empty, otherwise None

    Note:
        For even-length lists, the second middle node is returned.
    """
    # 100 - 200 - 300 - 400 - 500
    if dll.is_empty():
        raise ValueError("Get Middle Node Failed: the link list is empty.")

    slow = dll.head
    fast = dll.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def get_nth_from_start(dll, n):
    """
    Function: Get the nth node from the start of the linked list
    :param dll: Doubly linked list instance
    :param n: Zero-based index from the start
    :return: Node at the given position if found, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Get Nth Failed: the linked list is empty.")

    if n < 0:
        return None
    curr_node = dll.head
    while curr_node and n > 0:
        curr_node = curr_node.next
        n -= 1

    return curr_node


def get_nth_from_end(dll, n):
    """
    Function: Get the nth node from the end of the linked list
    :param dll: Doubly linked list instance
    :param n: Zero-based index from the end
    :return: Node at the given position if found, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Get Nth Failed: the linked list is empty.")

    if n < 0:
        return None

    curr_node = dll.tail
    while curr_node and n > 0:
        curr_node = curr_node.prev
        n -= 1

    return curr_node
