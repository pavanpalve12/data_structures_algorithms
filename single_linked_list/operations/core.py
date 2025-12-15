"""
Module: core
------------------------
Provides core utility functions and decorators for working with singly linked lists.

This module contains helper functions used to manage and display a linked list,
including traversal, emptiness checks, clearing nodes, and formatted printing.
It also defines a `pretty_print` decorator that formats console output when
printing the contents of a linked list.

Functions:
    pretty_print(func):
        Decorator that formats linked list output between labeled dividers.
    is_empty(ll_obj):
        Check whether the linked list is empty.
    traverse(ll_obj):
        Traverse the linked list, returning node values, length, and a string representation.
    clear_linked_list(ll_obj):
        Remove all nodes and reset the list to an empty state.
    print_linked_list(ll_obj):
        Print a formatted representation of the linked list to the console.

Example:
    --------------------------- Linked List ---------------------------
    HEAD -> 10 -> 20 -> 30 -> None
    -------------------------------------------------------------------

Notes:
    - All functions assume the linked list object defines:
        • `head` – reference to the first node in the list
        • `is_empty()` – method returning True if the list has no nodes
    - Errors for empty lists should raise appropriate exceptions rather than strings.
"""
from functools import wraps
def pretty_print(func):
    """
    Function: Decorator function for printing linked list
    :param func: print_linked_list
    :return: Nothing
    :Example:
    ---------------- Linked List -----------------
    HEAD -> 100 -> 200 -> TAIL
    ----------------------------------------------
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{'-' * 35} Linked List {'-' * 35}")
        func(*args, **kwargs)
        print(f"{'-' * (70 + len(" Linked List "))}")
    return wrapper

def is_empty(ll_obj) -> bool:
    """
    Check whether the linked list is empty.

    Returns:
       bool: True if the linked list has no nodes, False otherwise.
    """
    if ll_obj.head:
        return False

    return True

def traverse(ll_obj) -> dict:
    """
    Traverse the linked list and collect its elements.

    Returns:
        dict: A dictionary containing:
            - 'values' (list): All node data values in traversal order.
            - 'length' (int): Total number of nodes traversed.
            - 'str_repr' (str): String representation of the linked list,
              typically in the format "data1 -> data2 -> data3".
    """
    if ll_obj.is_empty():
        raise ValueError("Linked list is empty. Traversal is not possible.")
    ll_info = {}
    length = 0
    values = []
    ll_str = "Head -> "

    curr_node = ll_obj.head
    while curr_node:
        length += 1
        values.append(curr_node.data)
        ll_str += f"{curr_node.data} -> "
        curr_node = curr_node.next

    ll_str += "None"

    ll_info['values'] = values
    ll_info['length'] = length
    ll_info['str_repr'] = ll_str

    return ll_info

def clear_linked_list(ll_obj) -> bool:
    """
    Remove all nodes from the linked list and reset it to empty.

    Returns:
        bool: True if the list is empty after clearing.
    """
    ll_obj.head = None
    return is_empty(ll_obj)

@pretty_print
def print_linked_list(ll_obj):
    """
    Print a formatted representation of the linked list contents.
    """
    ll_info = ll_obj.traverse()
    print(ll_info['str_repr'])
