"""
------------------------------------------------------------------------------------
Module Name: traversal
------------------------------------------------------------------------------------

This module defines traversal operations for a doubly linked data structure.

Available functions:
- traverse_forward
- traverse_backward
- traverse_from_node_forward
- traverse_from_node_backward

The implementation is intentionally minimal and provides placeholder
functions only, without concrete traversal logic.
------------------------------------------------------------------------------------
"""


def traverse_forward(dll):
    """
    Traverse the structure from head to tail.
    :param dll: The first node in the structure.
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Traverse Forward Failed: the linked list is empty.")

    curr_node = dll.head
    while curr_node:
        print(f"{curr_node.data}", end= " <-> ")
        curr_node = curr_node.next

def traverse_backward(dll):
    """
    Traverse the structure from tail to head.
    :param dll: The last node in the structure.
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Traverse Backward Failed: the linked list is empty.")

    curr_node = dll.tail
    while curr_node:
        print(f"{curr_node.data}", end=" <-> ")
        curr_node = curr_node.prev

def traverse_from_node_forward(dll, node):
    """
    Traverse forward starting from a given node.
    :param dll: The node to start traversal from.
    :param node: The node to start traversal from.
    :type node: Any
    :return: None
    """
    if not node:
        raise ValueError("Traverse Failed: the node is invalid.")

    while node:
        print(f"{node.data}", end=" <-> ")
        node = node.next

def traverse_from_node_backward(dll, node):
    """
    Traverse backward starting from a given node.
    :param node: The node to start traversal from.
    :param dll: The node to start traversal from.
    :type node: Any
    :return: None
    """
    if not node:
        raise ValueError("Traverse Failed: the node is invalid.")

    while node:
        print(f"{node.data}", end=" <-> ")
        node = node.prev
