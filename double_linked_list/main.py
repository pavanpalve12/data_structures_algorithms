"""
Module: main
------------
Entry point for testing and demonstrating doubly linked list operations.

This script exercises the `DoubleLinkedList` and `Node` abstractions defined in
`doubly_linked_list.schemas`. It validates bidirectional traversal, insertion,
deletion, search, update, and structural integrity operations.

The goal is to verify correctness of pointer management (prev/next) and ensure
head and tail invariants are preserved across all operations.

Example:
    from doubly_linked_list.schemas import DoubleLinkedList

    if __name__ == "__main__":
        dll = DoubleLinkedList()
        dll.insert_at_head(10)
        dll.insert_at_tail(20)
        dll.insert_at_tail(30)
        dll.print_linked_list()
        print(dll.traverse_forward())
        print(dll.traverse_backward())
        dll.clear()

Output:
    ----------------------- Doubly Linked List ------------------------
    Head <-> 10 <-> 20 <-> 30 <-> None
    ------------------------------------------------------------------
    {'values': [10, 20, 30], 'length': 3}
    {'values': [30, 20, 10], 'length': 3}

Notes:
    - Intended for manual verification and debugging
    - Structural validation helpers should be invoked during testing
    - Replace print statements with logging in production env
"""

from double_linked_list.schemas import DoubleLinkedList, Node


def main():
    dll1 = DoubleLinkedList()
    values = "Z B D T U P".split(" ")
    dll1.from_list(values)
    dll1.print_linked_list()

    dll1.sort_ascending()
    dll1.print_linked_list()

    dll1.sort_descending()
    dll1.print_linked_list()

if __name__ == "__main__":
    main()

    """
        n1 = Node(100)
        n2 = Node(200)
        n3 = Node(300)
        n4 = Node(400)

        n1.next = n2
        n2.next = n3
        n3.next = n1
        n4.next = None

        n1.prev = None
        n2.prev = n1
        n3.prev = n2
        n4.prev = n3

        dll.head = n1
        dll.tail = n4
    """