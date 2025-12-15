"""
Module: helpers
---------------
Provides high-level helper and conversion functions for linked list operations.

These helper functions focus on convenience and interoperability — converting
between linked lists and Python built-ins, cloning, comparing, and data cleanup.
They complement the core and utility operation modules by offering additional
ease-of-use functionality for testing, visualization, and data preparation.

Functions included:
    - to_list(ll_obj)
    - from_list(ll_obj, data_list)
    - compare_lists(ll_obj, other)
    - clone(ll_obj)
    - remove_duplicates(ll_obj)
    - get_max(ll_obj)
    - get_min(ll_obj)
    - print_reverse(ll_obj)

Notes:
    - All functions operate on LinkedList objects that expose `.head` attributes.
    - Functions are designed for simplicity and readability over raw performance.
"""

from typing import Any


def to_list(ll_obj) -> list:
    """
    Function: Convert a linked list into a Python list of node values.
    :param ll_obj: The linked list object to convert.
    :return: A Python list containing all node values in order.
    """
    ll_info = ll_obj.traverse()
    print(f"Linked List to Python List -> {ll_info['values']}")
    return ll_info['values']


def from_list(ll_obj, data_list: list):
    """
    Function: Build or reset a linked list from a Python list.
    :param ll_obj: The linked list object to populate.
    :param data_list: A Python list of values to insert as nodes.
    :return: The updated linked list instance.
    """
    for idx, node in enumerate(data_list):
        if idx == 0:
            ll_obj.insert_node_at_head(node)
        else:
            ll_obj.insert_node_at_end(node)

    ll_obj.print_linked_list()
    return ll_obj


def compare_lists(ll_obj, other) -> bool:
    """
    Function: Compare two linked lists for data equality with optional rules.
    :param ll_obj: The first linked list to compare.
    :param other: The second linked list to compare.
    :return: True if both linked lists match under the chosen comparison rules, else False.
    """
    ll_info = ll_obj.traverse()
    other_info = other.traverse()

    if ll_info['values'] == other_info['values']:
        print(
            f"Linked Lists, \nL1: {ll_info['str_repr']} \n"
            f"L2: {other_info['str_repr']}\n"
            "List are equal."
        )
        return True
    print(
        f"Linked Lists, \nL1: {ll_info['str_repr']} \n"
        f"L2: {other_info['str_repr']}\n"
        "List are not equal."
    )
    return False


def clone(ll_obj, source_obj):
    """
    Function: Create and return a deep copy of the linked list.
    :param ll_obj: The linked list object to clone.
    :param source_obj: The other empty linked list object
    :return: A new linked list containing the same data values.
    """
    ll_info = source_obj.traverse()
    values = ll_info['values']

    head = ll_obj.from_list(values)
    head.print_linked_list()
    return head


def remove_duplicates(ll_obj):
    """
    Function: Remove duplicate node values from the linked list.
    :param ll_obj: The linked list object to modify.
    :return: The updated linked list instance without duplicates.
    """
    ll_info = ll_obj.traverse()
    values = ll_info['values']
    seen = []
    for node in values:
        if node not in seen:
            seen.append(node)

    ll_obj.remove_all_nodes()
    head = ll_obj.from_list(seen)
    head.print_linked_list()
    return head


def get_max(ll_obj) -> Any:
    """
    Function: Retrieve the maximum data value from the linked list.
    :param ll_obj: The linked list object to analyze.
    :return: The maximum value found, or None if the list is empty.
    """
    ll_info = ll_obj.traverse()
    max_value = max(ll_info['values'])
    print(f"{max_value} is max value in linked list")
    return max_value


def get_min(ll_obj) -> Any:
    """
    Function: Retrieve the minimum data value from the linked list.
    :param ll_obj: The linked list object to analyze.
    :return: The minimum value found, or None if the list is empty.
    """
    ll_info = ll_obj.traverse()
    min_value = min(ll_info['values'])
    print(f"{min_value} is min value in linked list")
    return min_value


def print_reverse(ll_obj):
    """
    Function: Print the linked list nodes in reverse order without modifying it.
    :param ll_obj: The linked list object to print in reverse.
    :return: None
    """

    if not ll_obj.head:
        raise ValueError("Linked List is empty")

    fmt_str = "HEAD -> "
    def _reverse(node):
        nonlocal fmt_str
        if not node:
            return
        _reverse(node.next)
        fmt_str += f"{node.data} -> "

    _reverse(ll_obj.head)
    fmt_str += 'END'

    print(fmt_str)
