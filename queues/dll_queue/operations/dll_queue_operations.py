"""
------------------------------------------------------------------------------------
Module Name: dll_queue_operations
------------------------------------------------------------------------------------

This module implements all operational logic for the DLLQueue data structure.

It serves as the execution layer for queues behavior while keeping the DLLQueue
schema lightweight and focused solely on exposing the public API.

All functions in this module operate on a DLLQueue instance and directly
manipulate its underlying doubly linked list structure.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement core queues operations using a doubly linked list
- Maintain structural integrity of node links (next / prev)
- Enforce FIFO (First-In-First-Out) semantics
- Isolate all queues business logic away from the schema layer

------------------------------------------------------------------------------------
Core Queue Operations
------------------------------------------------------------------------------------
- insert_at_head -> Insert a new element at the head of the linked list
- delete_at_tail -> Remove and return the element at the tail of the linked list
- get_value_at_head -> Return the value at the head without removing it
- is_empty -> Check whether the queues is empty
- size -> Return the number of elements in the queues
- clear -> Remove all elements from the queues

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_linked_list -> Print queues contents from front to rear

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a DLLQueue instance as the first argument
- Node traversal and pointer updates are handled exclusively here
- No function mutates schema-level definitions
- No I/O is performed except explicitly documented utilities
- Placeholder implementations are provided for incremental development

------------------------------------------------------------------------------------
"""
from typing import Any

def insert_at_head(dll, new_node) -> bool:
    """
    Insert a new element at the head of the doubly linked list.
    This operation corresponds to enqueue behavior in the queues abstraction.
    :param dll: DLLQueue instance on which the operation is performed
    :param new_node: Element to be inserted into the queues
    :return: return True on success else False
    """
    if dll.is_empty():
        dll.head = new_node
        dll.tail = dll.head
        dll.head.prev, dll.tail.next, dll.size = None, None, dll.size + 1
        new_node.next, new_node.prev = None, None
        return True

    new_node.next = dll.head
    new_node.prev = None
    dll.head.prev = new_node
    dll.head = new_node
    dll.head.prev = None
    dll.size = dll.size + 1

    return True

def delete_at_tail(dll) -> Any:
    """
    Remove and return the element at the tail of the doubly linked list.
    This operation corresponds to dequeue behavior in the queues abstraction.
    :param dll: DLLQueue instance on which the operation is performed
    :return: Placeholder return value
    """
    if dll.is_empty():
        raise ValueError("Dequeue Failed: the queues is empty.")

    deleted_tail = dll.tail

    if dll.tail == dll.head:
        dll.head, dll.tail, dll.size = None, None, dll.size - 1
        return deleted_tail

    prev_node = dll.tail.prev
    dll.tail = prev_node
    dll.tail.next = None
    dll.size = dll.size - 1

    deleted_tail.prev, deleted_tail.next = None, None
    return deleted_tail.data

def get_value_at_tail(dll) -> Any:
    """
    Return the value stored at the head of the linked list without removing it.
    This operation corresponds to peek behavior in the queues abstraction.
    :param dll: DLLQueue instance on which the operation is performed
    :return: Placeholder return value
    """
    if dll.is_empty():
        raise ValueError("Peek Failed: the queues is empty")
    return dll.tail.data

def is_empty(dll) -> bool:
    """
    Check whether the queues is empty.
    :param dll: DLLQueue instance on which the operation is performed
    :return: Placeholder boolean value
    """
    return not dll.head

def size(dll) -> int:
    """
    Return the number of elements currently present in the queues.
    :param dll: DLLQueue instance on which the operation is performed
    :return: Placeholder integer value
    """
    return dll.size

def clear(dll) -> bool:
    """
    Remove all elements from the queues and reset its state.
    :param dll: DLLQueue instance on which the operation is performed
    :return: Placeholder boolean value
    """
    dll.head, dll.tail, dll.size = None, None, 0
    return dll.is_empty()

def print_linked_list(dll):
    """
    Print the contents of the queues from front to rear.
    This utility function is intended for debugging and demonstration.
    :param dll: DLLQueue instance on which the operation is performed
    :return: None
    """
    if dll.is_empty():
        print("Queue is empty.")
        return

    queue_body = "Head → |"
    curr_node = dll.head
    while curr_node:
        if curr_node == dll.head:
            queue_body += f" {curr_node.data} |"
        else:
            queue_body += f" ←→ | {curr_node.data} |"
        curr_node = curr_node.next

    title = " Queue "
    queue_body += " ← Tail"
    width = max(len(title), len(queue_body)) + 8
    header = f"{title.center(width, '-')}"
    footer = "-" * width
    print(
        f"{header}"
        f"\n\t{queue_body}"
        f"\n{footer}"
        f"\n\tRear → {dll.head.data}"
        f"{("Front → " + str(dll.tail.data)).rjust(width - 8 - len(f"Rear → {dll.head.data}"), ' ')}"
        f"\n{footer}"
    )
