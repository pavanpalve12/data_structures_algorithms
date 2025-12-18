"""
------------------------------------------------------------------------------------
Module Name: validation_operations
------------------------------------------------------------------------------------

This module defines validation and integrity-check operations for a doubly
linked list (DLL).

These utilities are intended to verify the structural correctness of the list
after mutation operations such as insert, delete, swap, or relink.

Available functions:
- validate_dll_structure
- check_forward_backward_consistency
- detect_cycle
- verify_head_tail_integrity

All functions expect the doubly linked list (dll) to be passed explicitly as
the first argument.

Note:
These functions are designed as validation helpers and do not modify node data.
------------------------------------------------------------------------------------
"""


def validate_dll_structure(dll):
    """
    Perform a full structural validation of the doubly linked list.

    This function acts as a coordinator that invokes all individual
    validation checks, including:
    - forward/backward link consistency
    - cycle detection
    - head and tail integrity verification

    :param dll: Doubly linked list object
    :return: True if the list passes all validations, otherwise raises an error
    """
    dll.verify_head_tail_integrity()
    dll.detect_cycle()
    dll.check_forward_backward_consistency()

    return True


def check_forward_backward_consistency(dll):
    """
    Verify that forward and backward links between nodes are consistent.

    Ensures that:
    - for every node, node.next.prev == node
    - for every node, node.prev.next == node

    Any mismatch indicates structural corruption.

    :param dll: Doubly linked list object
    :return: True if links are consistent, otherwise raises an error
    """
    if dll.is_empty():
        return True

    dll.verify_head_tail_integrity()

    curr_node = dll.head
    while curr_node:
        next_node = curr_node.next
        prev_node = curr_node.prev

        if prev_node and prev_node.next != curr_node:
            raise ValueError(f"Validate Failed: broken backward link at node {curr_node.data}")
        if next_node and next_node.prev != curr_node:
            raise ValueError(f"Validate Failed: broken forward link at node {curr_node.data}")
        curr_node = curr_node.next
    return True


def detect_cycle(dll):
    """
    Detect whether the doubly linked list contains a cycle.

    Cycles indicate corruption and can cause infinite traversal loops.
    This check ensures the list is acyclic in the forward direction.

    :param dll: Doubly linked list object
    :return: True if no cycle is detected, otherwise raises an error
    """
    if dll.is_empty():
        return True

    slow_walker = dll.head
    fast_walker = dll.head
    while fast_walker and fast_walker.next:
        slow_walker = slow_walker.next
        fast_walker = fast_walker.next.next

        if slow_walker == fast_walker:
            raise ValueError("Cycle is detected.")

    return True

def verify_head_tail_integrity(dll) -> bool:
    """
    Verify head and tail boundary conditions of the doubly linked list.

    Ensures that:
    - dll.head.prev is None
    - dll.tail.next is None

    Violations indicate an invalid list boundary configuration.

    :param dll: Doubly linked list object
    :return: True if head and tail are valid, otherwise raises an error
    """
    if not dll.head.prev is None:
        raise ValueError("Head is not in correct position.")
    if not dll.tail.next is None:
        raise ValueError("Tail is not in correct position.")
    return True
