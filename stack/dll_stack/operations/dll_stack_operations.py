"""
------------------------------------------------------------------------------------
Module Name: dll_stack_operations
------------------------------------------------------------------------------------

This module defines the operational logic layer for a Doubly Linked List (DLL)
based Stack implementation.

It contains placeholder implementations for all dll operations exposed by
the DLLStack public interface.

Responsibilities:
- Implement all core dll behaviors (push, pop, peek, etc.)
- Operate directly on the internal state of a DLLStack instance
- Enforce correct LIFO semantics and error handling
- Remain fully decoupled from the public dll interface

This module is intended to be used exclusively by the DLLStack class.
No dll state is maintained here directly.

------------------------------------------------------------------------------------
Core Stack Operations
------------------------------------------------------------------------------------
- push -> insert_at_tail
- pop -> delete_at_tail
- peek -> get_data_at_tail
- is_empty
- size
- clear

------------------------------------------------------------------------------------
Utility / Output Operations
------------------------------------------------------------------------------------
- print_stack -> print_linked_list

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All functions accept a DLLStack instance as the first argument
- All logic operates on the dll’s head and tail references
- No function performs direct I/O except print_stack
- This module defines behavior only, not structure
- Placeholder implementations raise NotImplementedError

------------------------------------------------------------------------------------
"""

from typing import Any

def insert_at_tail(dll, new_node):
    """
    Pushes an element onto the top of the dll.
    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :param new_node: Value to be pushed onto the dll
    :type new_node: Node
    :return: None
    """
    if dll.is_empty():
        dll.head = new_node
        dll.tail = dll.head
        dll.head.prev, dll.tail.next = None, None
        return

    dll.tail.next = new_node
    new_node.prev = dll.tail
    dll.tail = new_node
    dll.tail.next = None

def delete_at_tail(dll) -> Any:
    """
    Removes and returns the top element of the dll.
    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :return: Top element of the dll
    :rtype: any
    :raises ValueError: If the dll is empty
    """
    if dll.is_empty():
        raise ValueError("Delete at Tail Failed: the stack is empty.")

    deleted_tail = dll.tail
    if dll.tail == dll.head:
        dll.head, dll.tail = None, None
        return deleted_tail.data

    prev_node = dll.tail.prev
    dll.tail = prev_node
    dll.tail.next = None

    deleted_tail.next, deleted_tail.prev = None, None
    return deleted_tail.data

def get_data_at_tail(dll) -> Any:
    """
    Returns the top element of the dll without removing it.

    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :return: Top element of the dll
    :rtype: any
    """
    if dll.is_empty():
        raise ValueError("Get Tail Failed: the stack is empty.")
    return dll.tail.data

def is_empty(dll):
    """
    Checks whether the dll is empty.

    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :return: True if the dll is empty, False otherwise
    :rtype: bool
    :raises NotImplementedError: Operation not yet implemented
    """
    return not dll.head

def size(dll) -> int:
    """
    Returns the number of elements in the dll.

    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :return: Number of elements in the dll
    :rtype: int
    """
    length = 0
    if dll.is_empty():
        return length

    curr_node = dll.head
    while curr_node:
        length += 1
        curr_node = curr_node.next
    return length

def clear(dll) -> bool:
    """
    Removes all elements from the dll.
    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :return: True if stack is empty else False
    """
    if dll.is_empty():
        return True
    dll.head = None
    return dll.is_empty()

def print_linked_list(dll):
    """
    Prints the contents of the dll from bottom to top.

    :param dll: Stack instance to operate on
    :type dll: DLLStack
    :return: None
    """
    if dll.is_empty():
        print("Stack is empty")
        return

    stack_body = "Head → |"
    curr_node = dll.head
    while curr_node:
        if curr_node == dll.head:
            stack_body += f" {curr_node.data} |"
        else:
            stack_body += f" ←→ | {curr_node.data} |"
        curr_node = curr_node.next

    title = " Stack "
    stack_body += " ← Tail"
    width = max(len(stack_body), len(title)) + 8
    header = f"{title.center(width, '-')}"
    footer = "-" * width
    print(
        f"{header}"
        f"\n\t{stack_body}"
        f"\n{footer}"
        f"\n\tBottom → {dll.head.data}"
        f"{("Top → " + str(dll.tail.data)).rjust(width-8-len("Bottom → 100"), ' ')}"
        f"\n{footer}"
    )
