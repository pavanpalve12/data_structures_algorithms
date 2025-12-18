"""
------------------------------------------------------------------------------------
Module Name: dll_queue_schemas
------------------------------------------------------------------------------------

This module defines the schema and public interface for a Queue implementation
backed by a Doubly Linked List (DLL).

It exposes lightweight container classes responsible for:
- defining node structure
- maintaining queue state via head reference
- exposing a FIFO queue interface
- delegating all operational logic to the operations module

All queue behavior and structural manipulation is implemented in the
`dll_queue_operations` module.

------------------------------------------------------------------------------------
Data Structures
------------------------------------------------------------------------------------
- Node     -> Doubly linked list node storing data and bidirectional links
- DLLQueue -> Queue abstraction implemented using a doubly linked list

------------------------------------------------------------------------------------
Core Queue Operations
------------------------------------------------------------------------------------
- enqueue -> Insert an element at the rear of the queue
- dequeue -> Remove and return the front element of the queue
- peek -> Return the front element without removing it
- is_empty -> Check whether the queue is empty
- size -> Return the number of elements in the queue
- clear -> Remove all elements from the queue

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_queue -> Print queue contents from front to rear

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- This module contains no queue business logic
- All operations are delegated to the operations layer
- Internal state is maintained via linked nodes
- The queue follows strict FIFO (First-In-First-Out) semantics
- The schema layer acts only as an interface and state holder

------------------------------------------------------------------------------------
"""

from queue.dll_queue.operations import dll_queue_operations


class Node:
    """
    Node represents a single element in a doubly linked list.

    Each node stores:
    - a data payload
    - a reference to the next node
    - a reference to the previous node

    Nodes are used internally by the DLLQueue structure.
    """

    def __init__(self, data):
        """
        Initialize a doubly linked list node.

        :return: None
        """
        self.data = data
        self.next = None
        self.prev = None


class DLLQueue:
    """
    DLLQueue represents a FIFO (First-In-First-Out) queue abstraction
    implemented using a doubly linked list.

    This class is responsible for:
    - maintaining the head reference of the linked list
    - exposing the public queue interface
    - delegating all queue operations to the operations module

    No queue logic is implemented directly in this class.
    """

    def __init__(self):
        """
        Initialize an empty doubly linked list based queue.

        :return: None
        """
        self.head = None
        self.tail = None
        self.size = 0

# ------------ Queue Operations ---------------------------------------------------------------
    def enqueue(self, data):
        """
        Insert an element at the rear of the queue.

        :param data: Element to be added to the queue
        :return: Result of the enqueue operation
        """
        new_node = Node(data)
        return dll_queue_operations.insert_at_head(self, new_node)

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        :return: The element removed from the front of the queue
        """
        return dll_queue_operations.delete_at_tail(self)

    def peek(self):
        """
        Return the front element of the queue without removing it.

        :return: The front element of the queue
        """
        return dll_queue_operations.get_value_at_tail(self)

    def is_empty(self):
        """
        Check whether the queue is empty.

        :return: True if the queue is empty, False otherwise
        """
        return dll_queue_operations.is_empty(self)

    def clear(self):
        """
        Remove all elements from the queue.

        :return: True if the queue is empty after clearing
        """
        return dll_queue_operations.clear(self)

    def get_size(self):
        """
        Return the number of elements currently in the queue.

        :return: Integer representing the queue size
        """
        return dll_queue_operations.size(self)

    def print_queue(self):
        """
        Print the contents of the queue from front to rear.

        :return: None
        """
        return dll_queue_operations.print_linked_list(self)
