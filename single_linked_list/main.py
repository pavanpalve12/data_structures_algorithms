"""
Module: main
------------
Entry point for testing and demonstrating singly linked list operations.

This script showcases the functionality of the `LinkedList` and `Node` classes
from `single_linked_list.schemas`, including core utilities, insertion, and
search operations.

Example:
    from single_linked_list.schemas import LinkedList

    if __name__ == "__main__":
        ll = LinkedList()
        ll.insert_node_at_head(100)
        ll.insert_node_at_end(200)
        ll.print_linked_list()
        print(ll.traverse())
        ll.clear()

Output:
    --------------------------- Linked List ---------------------------
    Head -> 100 -> 200 -> None
    -------------------------------------------------------------------
    {'values': [100, 200], 'length': 2, 'str_repr': 'Head -> 100 -> 200 -> None'}

Notes:
    Designed for quick manual testing; replace print statements with
    logging for production use.
"""

from single_linked_list.schemas import LinkedList


def main():
    """
    Purpose: Entry point for running linked list operations and demonstrations.
    Args: None
    Returns: None
    """
    values = [11, 22, 3, 4, 5, 5, 4, 6, 6, 7, 11, 22]

    linked_list2 = LinkedList()
    linked_list2.from_list(values)

    seen = []
    for node in values:
        if node not in seen:
            seen.append(node)
    print(seen)

    linked_list2.remove_duplicates()

    linked_list3 = LinkedList()
    linked_list3.clone(linked_list2)

    linked_list2.print_reverse()

if __name__ == "__main__":
    main()
