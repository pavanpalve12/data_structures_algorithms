# DequeStack — Deque-Based Stack Implementation

## Overview

`DequeStack` is a stack implementation built on top of Python’s
`collections.deque`. It follows strict **LIFO (Last-In-First-Out)** semantics
and exposes a clean, minimal public API.

The design enforces a clear separation between **interface** and
**implementation**: the `DequeStack` class defines the public-facing methods,
while all operational logic is delegated to a dedicated operations module.

---

## Design Principles

- Strict separation of concerns
- Minimal and explicit public API
- Predictable behavior with no hidden side effects
- Emphasis on correctness, clarity, and performance

---

## Architecture

- `stack/schemas.py`  
  Defines the `DequeStack` public interface

- `stack/operations/deque_stack_operations.py`  
  Implements all stack operations and business logic

- Internal state is maintained using a single `collections.deque` instance

---

## Data Structure

### DequeStack

A stack abstraction implemented using `collections.deque` where:
- the **right end of the deque** represents the **top of the stack**
- elements are added and removed in strict LIFO order
- push and pop operations run in **O(1)** time

---

## Core Stack Operations

| Operation  | Description |
|-----------|-------------|
| `push`    | Insert an element at the top of the stack |
| `pop`     | Remove and return the top element |
| `peek`    | Return the top element without removing it |
| `is_empty`| Check whether the stack is empty |
| `size`    | Return the number of elements in the stack |
| `clear`   | Remove all elements from the stack |

---

## Utility / Output Operations

| Operation      | Description |
|---------------|-------------|
| `print_stack` | Print stack contents from bottom to top |

---

## Usage Example

```python
from stack.schemas import DequeStack

stack = DequeStack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()   # Bottom → | 10 | 20 | 30 | ← Top

print(stack.pop())    # 30
print(stack.peek())  # 20
print(stack.size())  # 2

stack.clear()
print(stack.is_empty())  # True
```
---
## Design Notes

- Follows strict **LIFO (Last-In-First-Out)** behavior
- Uses `collections.deque` to guarantee **O(1)** push and pop operations
- No stack logic is implemented directly in the `DequeStack` class
- All operational behavior is delegated to the operations layer
- The internal deque is treated as a protected implementation detail and not exposed directly

---

## Intended Use

This implementation is suitable for:

- Learning and teaching stack data structures
- Algorithm practice and experimentation
- Situations where predictable and consistent performance is required

For production-grade usage, consider adding:

- Robust exception handling instead of relying on implicit behavior
- Logging in place of print statements
- Thread-safety mechanisms if concurrent access is required
