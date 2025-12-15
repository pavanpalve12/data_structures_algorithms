"""
Module: search
-------------------
Provides helper functions for locating nodes in a singly linked list.

This module contains utility functions that operate on a LinkedList
object to retrieve nodes based on position or value. All functions
assume the linked list implements the attributes:
    - head: reference to the first node in the list
    - is_empty(): method returning True if the list is empty

Each function raises a ValueError when the list is empty or when the
requested node cannot be found.
"""

def get_last_node(ll_obj):
    """
    Function: find last node
    :param ll_obj:
    :return: prev_node, last_node
    """
    if ll_obj.is_empty():
        raise ValueError("Linked list is empty. Traversal is not possible.")

    curr_node = ll_obj.head
    prev_node = None
    while curr_node.next:
        prev_node = curr_node
        curr_node = curr_node.next

    return prev_node, curr_node

def get_node_by_value(ll_obj, target_node):
    """
    Function: find node by data value
    :param ll_obj: LinkedList class object
    :param target_node: target node to be found
    :return: prev_node, target_node
    """
    if ll_obj.is_empty():
        raise ValueError("Linked list is empty. Traversal is not possible.")

    curr_node = ll_obj.head
    prev_node = ll_obj.head
    while curr_node:
        if curr_node.data == target_node:
            return prev_node, curr_node
        prev_node = curr_node
        curr_node = curr_node.next

    raise LookupError("Target node not found in linked list.")

def get_node_by_index(ll_obj, index):
    """
    Function: find node at index
    :param ll_obj: LinkedList class object
    :param index: integer index for target node
    :return: prev_node, target_node
    """
    if ll_obj.is_empty():
        raise ValueError("Linked list is empty. Traversal is not possible.")

    node_counter = 0
    prev_node = ll_obj.head
    curr_node = ll_obj.head
    while curr_node:
        if index == node_counter:
            return prev_node, curr_node
        node_counter += 1
        prev_node = curr_node
        curr_node = curr_node.next

    raise IndexError("Index is invalid.")
