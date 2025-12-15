"""
Linked List Deletion Operations Module

This module provides helper functions to remove nodes from a singly linked list.
All functions operate on an existing LinkedList object and assume that the list
structure and supporting methods are already implemented correctly.

Scope:
- Removal of nodes by position (head, end, index)
- Removal of a node by value (first occurrence)

Assumptions:
- `ll_obj` is a valid LinkedList instance.
- The LinkedList exposes:
    - `head` attribute
    - `get_last_node()` -> (prev_node, last_node)
    - `get_node_by_value(value)` -> (prev_node, target_node)
    - `get_node_by_index(index)` -> (prev_node, target_node)
- The caller ensures the list is non-empty and inputs are valid.
- Error handling (empty list, invalid index/value) is intentionally NOT handled here.

Return Value:
- Each function returns the removed Node object.

Design Note:
- These functions mutate the linked list in-place.
- Responsibility for validation and edge-case handling lies with the caller or
  higher-level list methods.
"""

def remove_node_at_head(ll_obj):
    """
    Function: removes head node
    :param ll_obj: LinkedList class object
    :return: removed Node
    """
    removed_node = ll_obj.head
    ll_obj.head = ll_obj.head.next

    print(f"node {removed_node.data} is removed from head.")
    return removed_node

def remove_node_at_end(ll_obj):
    """
    Function: removes node at end
    :param ll_obj: LinkedList class object
    :return: removed Node
    """
    prev_node, last_node = ll_obj.get_last_node()
    prev_node.next = None

    print(f"node {last_node.data} is removed at the end.")
    return last_node


def remove_node_by_value(ll_obj, target_node):
    """
    Function: removes first occurrence of Node
    :param ll_obj: LinkedList class object
    :param target_node: target node value
    :return: removed Node
    """
    prev_node, target_node = ll_obj.get_node_by_value(target_node)

    if target_node == ll_obj.head:
        ll_obj.head = ll_obj.head.next
    else:
        prev_node.next = target_node.next

    print(f"node {target_node.data} is removed by value {target_node.data}.")
    return target_node

def remove_node_at_index(ll_obj, index):
    """
    Function: removes node at an index
    :param ll_obj: LinkedList class object
    :param index: target index
    :return: removed node
    """
    prev_node, target_node = ll_obj.get_node_by_index(index)

    if ll_obj.head == target_node:
        ll_obj.head = ll_obj.head.next
    else:
        prev_node.next = target_node.next

    print(f"node {target_node.data} is removed at index {index}.")
    return target_node

def remove_all_nodes(ll_object):
    """
    Function: removes all elements from linked list
    :param ll_object: LinkedList class object
    :return: Nothing
    """
    ll_object.clear()
