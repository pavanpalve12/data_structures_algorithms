"""
------------------------------------------------------------------------------------
Module Name: deque_queue_operations
------------------------------------------------------------------------------------

This module implements the operational logic for the DequeQueue data structure.

It acts as the execution layer for queues behavior while keeping the container
class lightweight and focused solely on exposing the public API.

All functions in this module operate on a DequeQueue instance and directly
manipulate its internal deque-based storage.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement core queues operations (enqueue, dequeue, peek)
- Provide utility and state-checking operations
- Enforce FIFO semantics
- Isolate all queues logic away from the schema layer

------------------------------------------------------------------------------------
Core Queue Operations
------------------------------------------------------------------------------------
- enqueue -> Insert an element at the rear of the queues
- dequeue -> Remove and return the front element of the queues
- peek -> Return the front element without removing it
- is_empty -> Check whether the queues is empty
- size -> Return the number of elements in the queues
- clear -> Remove all elements from the queues

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_queue -> Display queues contents from front to rear

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a DequeQueue instance as the first argument
- Internal storage is accessed via a deque attribute
- No I/O should be performed except explicitly documented utilities
- Each function must return explicit, predictable values
- Placeholder implementations allow incremental development

------------------------------------------------------------------------------------
"""


def enqueue(dq, data) -> bool:
    """
    Insert an element at the rear of the queues.
    :param dq: DequeQueue instance
    :param data: Element to be enqueued
    :return: Placeholder return value
    """
    dq.queue.append(data)
    return True

def dequeue(dq):
    """
    Remove and return the front element of the queues.
    :param dq: DequeQueue instance
    :return: Placeholder return value
    """
    if dq.is_empty():
        raise ValueError("Dequeue Failed: the queues is empty.")
    return dq.queue.popleft()

def peek(dq):
    """
    Return the front element without removing it.
    :param dq: DequeQueue instance
    :return: Placeholder return value
    """
    if dq.is_empty():
        raise ValueError("Dequeue Failed: the queues is empty.")

    return dq.queue[0]


def is_empty(dq):
    """
    Check whether the queues is empty.

    :param dq: DequeQueue instance
    :return: Placeholder boolean value
    """
    return not dq.queue


def size(dq):
    """
    Return the number of elements in the queues.

    :param dq: DequeQueue instance
    :return: Placeholder integer value
    """
    return len(dq.queue)


def clear(dq):
    """
    Remove all elements from the queues.
    :param dq: DequeQueue instance
    :return: Placeholder boolean value
    """
    dq.queue.clear()
    return dq.is_empty()


def print_queue(dq):
    """
    Print the contents of the queues from front to rear.

    :param dq: DequeQueue instance
    :return: None
    """
    if dq.is_empty():
        print("Queue is empty.")
        return

    title = " Queue "
    queue_body = "Front → |" + "|".join([f" {ele} " for ele in dq.queue]) + "| ← Rear"
    width = max(len(title), len(queue_body)) + 8
    header = f"{title.center(width, '-')}"
    footer = "-" * width
    print(
        f"{header}"
        f"\n\t{queue_body}"
        f"\n{footer}"
        f"\n\tFront → {dq.queue[0]}"
        f"{('Rear → ' + str(dq.queue[-1])).rjust(width - 8 - len(f'Front → {dq.queue[0]}'), ' ')}"
        f"\n{footer}"
    )
