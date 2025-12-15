"""
linked_list_utilities
=====================

Utilities for working with singly linked lists backed by a `LinkedList` object
(assumed to expose `.head`, `.traverse() -> {'length': int, ...}`, and
`get_node_by_index(i) -> (prev, curr)`), and `Node`/`ListNode` nodes with
`.data` and `.next`.

What’s inside
-------------
- get_length(ll_obj): Return the number of nodes (prints the length too).
- reverse_linked_list(ll_obj): Reverse the list in place; updates and returns ll_obj.
- count_node_occurrences(ll_obj, target_node): Count nodes whose `.data` equals `target_node`.
- find_middle_node(ll_obj): Return the middle node(s); for even length returns (prev, curr), for odd returns (None, curr).
- find_nth_from_last(ll_obj, n): Return the n-th node from the end (1-based).
- merge_two_linked_lists(ll_obj, other): Interleave two lists by alternating nodes (mutates inputs).
- detect_cycle(ll_obj): Detect a cycle using a visited set; returns the node whose `.next` re-enters the seen set, or None.
- remove_cycle(ll_obj): If a cycle is detected (via `detect_cycle`), sever it by setting that node’s `.next = None`; returns ll_obj.

Behavior & assumptions
----------------------
- All functions operate **in place** unless otherwise stated; many update `ll_obj.head`.
- Empty lists trigger `ValueError` in operations where the action is undefined (e.g., reverse on empty).
- Time/space: typical linear-time traversals; `detect_cycle` uses O(n) extra space (visited set).
- The current `merge_two_linked_lists` **alternates nodes**; it does *not* sort/merge by value.

This module is intended for learning, diagnostics, and small utilities; adjust
APIs and error handling to your project’s conventions as needed.
"""


from typing import Any

def get_length(ll_obj) -> int:
    """
    Function: get length of linked list
    :param ll_obj: The linked list object to reverse.
    :return: length of linked list
    """
    ll_info = ll_obj.traverse()
    length = ll_info['length']
    print(f"Length of linked list is {length}.")
    return length

def reverse_linked_list(ll_obj):
    """
    Function: Reverse the given linked list.
    :param ll_obj: The linked list object to reverse.
    :return: The head node of the reversed linked list.
    """
    if not ll_obj.head:
        raise ValueError("Linked list is empty, cannot reverse")

    # 200 -> 300 -> 400 -> None
    # 100 -> None
    rev_head = None
    curr_node = ll_obj.head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = rev_head
        rev_head = curr_node
        curr_node = next_node

    ll_obj.head = rev_head
    ll_obj.print_linked_list()
    return ll_obj


def count_node_occurrences(ll_obj, target_node) -> int:
    """
    Function: Count the number of occurrences of a specific node in the linked list.
    :param ll_obj: The linked list object to search.
    :param target_node: The node to count within the linked list.
    :return: Integer count of occurrences.
    """
    if not ll_obj.head:
        raise ValueError("Linked list is empty, cannot count occurrences.")

    occ_count = 0
    curr_node = ll_obj.head
    while curr_node:
        if curr_node.data == target_node:
            occ_count += 1
        curr_node = curr_node.next

    print(f"Node {target_node} has {occ_count} occurrences in linked list")
    return occ_count

def find_middle_node(ll_obj) -> (Any, Any):
    """
    Function: Find the middle node of the linked list.

    :param ll_obj: The linked list object to analyze.
    :return: The middle node(s) of the linked list.

    Notes:
        - This function uses integer (floor) division `//` to find the middle index.
          For example, 5 // 2 -> 2 (floor division rounds down to the smaller integer).
        - For even-length linked lists (e.g., length 6 -> 6 // 2 = 3),
          nodes at positions 2 and 3 are both considered middle nodes, so return both.
        - For odd-length linked lists (e.g., length 7 -> 7 // 2 = 3),
          the node at position 3 is the single middle node.
    """
    ll_info = ll_obj.traverse()
    length = ll_info['length']
    mid_index = length // 2

    prev_node, curr_node = ll_obj.get_node_by_index(mid_index)

    if length % 2 == 0:
        print(
            f"Middle nodes are {prev_node.data} -> {curr_node.data} "
            "since linked list has even length."
        )
        return prev_node, curr_node

    print(f"Middle node is {curr_node.data}.")
    return None, curr_node

def find_nth_from_last(ll_obj, n) -> Any:
    """
    Function: Find the nth node from the end of the linked list.
    :param ll_obj: The linked list object to traverse.
    :param n: The position from the end (1-based index).
    :return: The nth node from the end of the list.
    """
    if n == 0:
        raise IndexError("Invalid index provided.")
    ll_info = ll_obj.traverse()
    length = ll_info['length']
    target_index = length - n

    _, target_node = ll_obj.get_node_by_index(target_index)
    print(f"{n}th node from last is {target_node.data}")
    return target_node

def merge_two_linked_lists(ll_obj, other):
    """
    Function: Merge two sorted linked lists into a single sorted linked list.
    :param ll_obj: The first sorted linked list.
    :param other: The second sorted linked list.
    :return: The head node of the merged linked list.
    """
    if not ll_obj.head or not other.head:
        raise ValueError("Either of the two or both linked lists are empty.")

    node1 = ll_obj.head
    node2 = other.head
    merged = ll_obj

    while node1 and node2:
        next_node1, next_node2 = node1.next, node2.next

        # Link current first list to current second list
        node1.next = node2

        if not next_node1:
            break

        # Link current second list to next of first list
        node2.next = next_node1

        # increment
        node1, node2 = next_node1, next_node2


    merged.print_linked_list()


def detect_cycle(ll_obj):
    """
    Function: Detect if there is a cycle in the linked list.
    :param ll_obj: The linked list object to check.
    :return: The node where the cycle begins, or None if no cycle exists.
    """
    if not ll_obj:
        raise ValueError("Linked list is empty.")

    visited_nodes = set()
    prev_node = None
    cycle_flag = False

    curr_node = ll_obj.head
    while curr_node:
        if curr_node in visited_nodes:
            cycle_flag = True
            break

        visited_nodes.add(curr_node)
        prev_node = curr_node
        curr_node = curr_node.next

    if cycle_flag:
        print(f"Cycle detected between nodes {prev_node.data} -> {prev_node.next.data}")
        return prev_node

    return None

def remove_cycle(ll_obj):
    """
    Function: Remove a cycle from the linked list if it exists.
    :param ll_obj: The linked list object to modify.
    :return: The head node of the modified (cycle-free) linked list.
    """
    cyclic_node = ll_obj.detect_cycle()
    if cyclic_node:
        cyclic_node.next = None
        print(f"Cycle is fixed, node {cyclic_node.data} now point to None.")

    return ll_obj
