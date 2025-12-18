"""
------------------------------------------------------------------------------------
Module Name: list_stack_operations
------------------------------------------------------------------------------------

This module implements all operational logic for the ListStack data structure.

It serves as the execution layer for stack behavior while keeping the ListStack
class itself lightweight and focused on exposing the public API.

All functions in this module operate on a ListStack instance and directly
manipulate its internal list-based storage.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement core stack operations (push, pop, peek)
- Provide utility and state-checking operations
- Enforce LIFO semantics and structural consistency
- Isolate all business logic away from the container class

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a ListStack instance as the first argument
- The internal storage is accessed via `stack.stack`
- No function performs I/O except explicitly documented utilities
- Placeholder implementations are provided for incremental development
- Each function must return predictable, explicit values

------------------------------------------------------------------------------------
"""

from typing import Any

def push(ls, data) -> bool:
    """
    Function: Push a data element onto the top of the stack.
    :param ls: ListStack instance
    :param data: Data element to be pushed
    :return: True if push succeeds, False otherwise
    """
    ls.stack.append(data) # if append fails, python will raise exception
    return True

def pop(ls) -> Any:
    """
    Function: Remove and return the top element from the stack.
    :param ls: ListStack instance
    :return: Top data element if stack is not empty, otherwise None or error
    """
    return ls.stack.pop()

def peek(ls) -> Any:
    """
    Function: Return the top element of the stack without removing it.
    :param ls: ListStack instance
    :return: Top data element if stack is not empty, otherwise None
    """
    return ls.stack[-1]

def is_empty(ls) -> bool:
    """
    Function: Check whether the stack is empty.
    :param ls: ListStack instance
    :return: True if stack is empty, False otherwise
    """
    if ls.size() == 0:
        return True
    return False

def size(ls) -> int:
    """
    Function: Return the number of elements in the stack.
    :param ls: ListStack instance
    :return: Integer size of the stack
    """
    return len(ls.stack)

def clear(ls) -> bool:
    """
    Function: Remove all elements from the stack.
    :param ls: ListStack instance
    :return: True if stack is empty after clearing, False otherwise
    """
    ls.stack.clear()
    return True

def print_stack(ls) -> None:
    """
    Function: Print the stack contents from bottom to top.
    :param ls: ListStack instance
    :return: None
    """
    if ls.is_empty():
        print("Stack is empty.")
        return

    stack_body = 'Bottom → |' + '|'.join([f" {e} " for e in ls.stack]) + '| ← Top'
    title = ' Stack '
    width = max(len(stack_body), len(title)) + 8
    header = f"{title.center(width, '-')}"
    footer = '-' * width
    print(
        f"{header}"
        f"\n\t{stack_body}" 
        f"\n{footer}"
        f"\n\tBottom → {ls.stack[0]} & Top → {ls.stack[-1]}\n{footer}"
    )
