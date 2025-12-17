"""
------------------------------------------------------------------------------------
Module: Core Functions
------------------------------------------------------------------------------------
This module provides helper functions and decorators for operating on a
doubly linked list, including traversal, validation, printing, and
state management. The functions are designed to work with a doubly
linked list implementation that exposes a `head` attribute.
------------------------------------------------------------------------------------
Available Functions:
    - traverse(dll) -> dict
        Traverses the list from head to tail and returns structural details.
    - is_empty(dll) -> bool
        Checks whether the linked list is empty.
    - clear(dll) -> bool
        Removes all nodes from the linked list.
    - print_linked_list(dll) -> None
        Prints the linked list in a formatted, human-readable form.
------------------------------------------------------------------------------------
"""

def traverse(dll) -> dict:
    """
    Function: Traverse the linked list from head to tail
    :param dll: Doubly linked list instance
    :return: Dictionary containing traversal details
             {
                 'values': list of node values,
                 'length': total number of nodes,
                 'str_repr': string representation of the list
             }
    """
    if dll.is_empty():
        raise ValueError("Traversal failed: the linked list is empty.")

    # validate if dll structure is correct
    # valid head & tail, no cycles and forward backward links are valid
    # it will raise error if something is invalid
    dll.validate_dll_structure()

    dll_info = {}
    length = 0
    values = []

    curr_node = dll.head
    while curr_node:
        length += 1
        values.append(curr_node.data)
        curr_node = curr_node.next

    dll_info['values'] = values
    dll_info['length'] = length
    dll_info['str_repr'] = "None ← " + " ←→ ".join(str(val) for val in values) + " → None"

    return dll_info


def is_empty(dll) -> bool:
    """
    Function: Check whether the linked list is empty
    :param dll: Doubly linked list instance
    :return: True if the list contains no nodes, otherwise False
    """
    return dll.head is None


def clear(dll) -> bool:
    """
    Function: Remove all nodes from the linked list
    :param dll: Doubly linked list instance
    :return: True if the list is cleared successfully, otherwise False
    """
    if not dll.is_empty():
        dll.head = None
    return dll.is_empty()

def print_linked_list(dll):
    """
    Function: Print the linked list with a dynamically sized header and footer
    :param dll: Doubly linked list instance
    :return: None

    The header and footer lengths are derived from the actual string
    representation of the linked list.
    """
    dll_info = dll.traverse()

    body = dll_info['str_repr']
    title = " Double Linked List "
    width = max(len(body), len(title)) + 8

    header = f"{title.center(width, '-')}"
    footer = "-" * width
    print(header)
    print(f"\t{body}")
    print(footer)
    print(f"\tHead -> {dll.head.data}, Tail -> {dll.get_last_node().data}")
    print(footer)



