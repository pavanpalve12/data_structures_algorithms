"""
------------------------------------------------------------------------------------
Module: Doubly Linked List Search Operations
------------------------------------------------------------------------------------
This module defines search-related operations for a doubly linked list.
Each function performs a specific lookup task without modifying the
structure of the list.
------------------------------------------------------------------------------------
Available Functions:
    - search_by_value(dll, value)
    - search_by_index(dll, index)
    - search_first_occurrence(dll, value)
    - search_last_occurrence(dll, value)
    - contains(dll, value)
    - get_last_node(dll)
------------------------------------------------------------------------------------
"""

def search_by_value(dll, value):
    """
    Function: Search for a node by value
    :param dll: Doubly linked list instance
    :param value: Value to search for
    :return: Node containing the value if found, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Search By Value Failed: the linked list is empty.")

    if not dll.contains(value):
        raise LookupError("Search By Value Failed: the value not found in linked list.")

    curr_node = dll.head
    while curr_node:
        if curr_node.data == value:
            return curr_node
        curr_node = curr_node.next

    return None

def search_by_index(dll, index):
    """
    Function: Search for a node by index
    :param dll: Doubly linked list instance
    :param index: Zero-based position to search
    :return: Node at the given index if found, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Search By Index Failed: the linked list is empty.")

    if not dll.traverse()['length'] > index > -1:
        raise IndexError("Search By Index Failed: index is invalid.")

    curr_node = dll.head
    itr_counter = 0
    while curr_node:
        if itr_counter == index:
            return curr_node
        itr_counter += 1
        curr_node = curr_node.next

    return None

def search_first_occurrence(dll, value):
    """
    Function: Find the first occurrence of a value
    :param dll: Doubly linked list instance
    :param value: Value to search for
    :return: First node containing the value if found, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Search Last Occurrence Failed: the linked list is empty.")

    curr_node = dll.head
    while curr_node:
        if curr_node.data == value:
            return curr_node
        curr_node = curr_node.next

    raise LookupError("Search Last Occurrence Failed: the value is not in linked list")

def search_last_occurrence(dll, value):
    """
    Function: Find the last occurrence of a value
    :param dll: Doubly linked list instance
    :param value: Value to search for
    :return: Last node containing the value if found, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Search Last Occurrence Failed: the linked list is empty.")

    curr_node = dll.tail
    while curr_node:
        if curr_node.data == value:
            return curr_node
        curr_node = curr_node.prev

    raise LookupError("Search Last Occurrence Failed: the value is not in linked list")

def contains(dll, value) -> bool:
    """
    Function: Check whether a value exists in the linked list
    :param dll: Doubly linked list instance
    :param value: Value to check for existence
    :return: True if value exists in the list, otherwise False
    """
    dll_info = dll.traverse()
    return value in dll_info['values']

def get_last_node(dll):
    """
    Function: Retrieve the last node in the linked list
    :param dll: Doubly linked list instance
    :return: Last node if the list is not empty, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Get Last Node Failed: linked list is empty")

    return dll.tail