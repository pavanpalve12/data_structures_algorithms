# ListStack — List-Based Stack Implementation

## Overview

`ListStack` is a clean and minimal implementation of a stack data structure
backed by Python’s native list type. It follows strict **LIFO
(Last-In-First-Out)** semantics and exposes a simple, predictable public API.

The design intentionally separates **interface** from **implementation**:
the `ListStack` class defines the public-facing methods, while all operational
logic is delegated to a dedicated operations module.

---

## Design Principles

- Clear separation of concerns
- Minimal, explicit API
- Predictable behavior with no hidden side effects
- Focus on correctness and readability over cleverness

---

## Architecture

- `stack/schemas.py`  
  Defines the `ListStack` public interface

- `stack/operations/list_stack_operations.py`  
  Implements all stack operations and business logic

- Internal state is maintained using a single Python list

---

## Data Structure

### ListStack

A stack abstraction implemented using a Python list where:
- the **end of the list** represents the **top of the stack**
- elements are added and removed in strict LIFO order

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
from stack.schemas import ListStack

stack = ListStack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.print_stack()   # [10, 20, 30]

print(stack.pop())    # 30
print(stack.peek())  # 20
print(stack.size())  # 2

stack.clear()
print(stack.is_empty())  # True
```
---
## Design Notes
- Follows strict LIFO (Last-In-First-Out) behavior
- No stack logic is implemented directly in the ListStack class
- All behavior is delegated to the operations layer
- The internal list is treated as a protected implementation detail
- Emphasizes clarity, predictability, and correctness over shortcuts

---
## Intended Use
This implementation is suitable for:
- Learning and teaching data structures
- Algorithm practice and experimentation
- Controlled environments where readability and correctness matter

For production-grade usage, consider adding:
- Robust exception handling
- Logging instead of print statements
- Thread-safety if concurrent access is required

---