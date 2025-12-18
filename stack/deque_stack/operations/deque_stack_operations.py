"""
------------------------------------------------------------------------------------
Module Name: deque_stack_operations
------------------------------------------------------------------------------------

This module implements all operational logic for the DequeStack data structure.

It acts as the execution layer for stack behavior while keeping the DequeStack
class focused solely on exposing the public interface.

All functions operate on a DequeStack instance and directly manipulate its
internal `collections.deque` storage.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement core stack operations (push, pop, peek)
- Provide utility and state-checking operations
- Enforce strict LIFO semantics
- Isolate all stack logic away from the container class

------------------------------------------------------------------------------------
Function List
------------------------------------------------------------------------------------
- push -> Insert an element at the top of the stack
- pop -> Remove and return the top element of the stack
- peek -> Return the top element without removing it
- is_empty -> Check whether the stack is empty
- size -> Return the number of elements in the stack
- clear -> Remove all elements from the stack
- print_stack -> Print stack contents from bottom to top

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions expect a DequeStack instance as the first argument
- The internal deque is accessed via `stack.stack`
- The right end of the deque represents the top of the stack
- No function implements business logic inside the container class
- Placeholder implementations support incremental development
- All functions must return explicit, predictable values

------------------------------------------------------------------------------------
"""

from typing import Any

def push(ds, data) -> bool:
    """
    Push a data element onto the top of the stack.

    :param ds: DequeStack instance
    :param data: Data element to be pushed
    :return: True if push succeeds, False otherwise
    """
    ds.stack.append(data)
    return True

def pop(ds) -> Any:
    """
    Remove and return the top element from the stack.

    :param ds: DequeStack instance
    :return: Top data element if stack is not empty, otherwise None
    """
    if ds.is_empty():
        raise ValueError("Pop Failed: the stack is empty.")

    return ds.stack.pop()

def peek(ds) -> Any:
    """
    Return the top element of the stack without removing it.

    :param ds: DequeStack instance
    :return: Top data element if stack is not empty, otherwise None
    """
    if ds.is_empty():
        raise ValueError("Peek Failed: the stack is empty.")

    return ds.stack[-1]

def is_empty(ds) -> bool:
    """
    Check whether the stack is empty.

    :param ds: DequeStack instance
    :return: True if stack is empty, False otherwise
    """
    return not ds.stack

def size(ds) -> int:
    """
    Return the number of elements in the stack.

    :param ds: DequeStack instance
    :return: Integer size of the stack
    """
    return len(ds.stack)

def clear(ds) -> bool:
    """
    Remove all elements from the stack.

    :param ds: DequeStack instance
    :return: True if stack is empty after clearing, False otherwise
    """
    ds.stack.clear()
    return ds.is_empty()

def print_stack(ds) -> None:
    """
    Print the stack contents from bottom to top.

    :param ds: DequeStack instance
    :return: None
    """
    if ds.is_empty():
        print("Stack is empty.")
        return
    title = " Stack "
    stack_body = 'Bottom → |' + '|'.join([f" {e} " for e in ds.stack]) + '| ← Top'
    width = max(len(stack_body), len(title)) + 8
    footer = "-" * width
    header = f"{title.center(width, '-')}"
    print(
        f"{header}"
        f"\n\t{stack_body}"
        f"\n{footer}"
        f"\n\tBottom → {ds.stack[0]} & Top → {ds.stack[-1]}\n{footer}"
    )
