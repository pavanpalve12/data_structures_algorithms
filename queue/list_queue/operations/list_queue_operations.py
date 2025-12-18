"""
------------------------------------------------------------------------------------
Module Name: list_queue_operations
------------------------------------------------------------------------------------

This module implements all operational logic for the ListQueue data structure.

It serves as the execution layer for queue behavior while keeping the ListQueue
class itself lightweight and focused on exposing the public API.

All functions in this module operate on a ListQueue instance and directly
manipulate its internal list-based storage.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement core queue operations (enqueue, dequeue, peek)
- Provide utility and state-checking operations
- Enforce FIFO semantics and structural consistency
- Isolate all business logic away from the container class

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
- print_queue -> Display queue contents from front to rear

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a ListQueue instance as the first argument
- The internal storage is accessed via `lq.queue`
- No function performs I/O except explicitly documented utilities
- Each function returns predictable, explicit values
- Error handling is minimal and intended for controlled usage

------------------------------------------------------------------------------------
"""

from typing import Any


def enqueue(lq, data) -> bool:
    """
    Insert an element at the rear of the queue.

    :param lq: ListQueue instance on which the operation is performed
    :param data: Element to be added to the queue
    :return: True if the element is successfully enqueued
    """
    lq.queue.append(data)
    return True


def dequeue(lq) -> Any:
    """
    Remove and return the front element of the queue.

    :param lq: ListQueue instance on which the operation is performed
    :return: The element removed from the front of the queue
    """
    if lq.is_empty():
        raise ValueError("Pop Failed: the queue is empty.")

    return lq.queue.pop(0)


def peek(lq) -> Any:
    """
    Return the front element of the queue without removing it.

    :param lq: ListQueue instance on which the operation is performed
    :return: The front element of the queue
    """
    if lq.is_empty():
        raise ValueError("Pop Failed: the queue is empty.")

    return lq.queue[0]


def is_empty(lq) -> bool:
    """
    Check whether the queue is empty.

    :param lq: ListQueue instance on which the operation is performed
    :return: True if the queue is empty, False otherwise
    """
    return not lq.queue


def size(lq) -> int:
    """
    Return the number of elements currently in the queue.

    :param lq: ListQueue instance on which the operation is performed
    :return: Integer representing the queue size
    """
    return len(lq.queue)


def clear(lq) -> bool:
    """
    Remove all elements from the queue.

    :param lq: ListQueue instance on which the operation is performed
    :return: True if the queue is empty after clearing
    """
    lq.queue.clear()
    return lq.is_empty()


def print_queue(lq):
    """
    Print the contents of the queue from front to rear.

    :param lq: ListQueue instance on which the operation is performed
    :return: None
    """
    if lq.is_empty():
        print("Queue is empty.")
        return

    title = " Queue "
    queue_body = "Front → |" + "|".join([f" {ele} " for ele in lq.queue]) + "| ← Rear"
    width = max(len(queue_body), len(title)) + 8
    header = f"{title.center(width, '-')}"
    footer = "-" * width
    print(
        f"{header}"
        f"\n\t{queue_body}"
        f"\n{footer}"
        f"\n\tFront → {lq.queue[0]}"
        f"{('Rear → ' + str(lq.queue[-1])).rjust(width - 8 - len(f'Front → {lq.queue[0]}'), ' ')}"
        f"\n{footer}"
    )
