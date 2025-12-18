# List-Based Queue Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular Queue implementation backed by a native
Python list**, designed with a strict separation of concerns.

The implementation follows **FIFO (First-In-First-Out)** semantics and mirrors
production-grade design principles by isolating:
- public interface (schemas)
- operational logic (operations)
- execution / validation (main)

This structure makes the queue easy to understand, test, extend, and later
replace with more efficient implementations (such as `collections.deque`)
without changing client code.

------------------------------------------------------------------------------------

## Architecture

queue/ <br>
└── list_queue/ <br> 
├── schemas.py      # Public Queue interface (no logic) <br>
├── operations.py   # Queue behavior & business logic <br>
└── main.py         # Entry point for testing and demonstration <br>

---

------------------------------------------------------------------------------------

## Design Philosophy

- **FIFO correctness first**
- **No logic in container classes**
- **All behavior delegated to operations layer**
- **Internal state managed via a single list**
- **Readable, predictable, and testable design**

This mirrors how real-world libraries separate interface from implementation.

------------------------------------------------------------------------------------

## Data Structure

### ListQueue

- Queue abstraction implemented using a Python list
- Enqueue operation appends at the list tail
- Dequeue operation removes from the list head
- Maintains internal state via a protected list attribute

⚠️ Note: Dequeue operations incur O(n) cost due to element shifting.

------------------------------------------------------------------------------------

## Core Queue Operations

| Operation | Description |
|---------|-------------|
| `enqueue` | Insert an element at the rear of the queue |
| `dequeue` | Remove and return the front element |
| `peek` | Return the front element without removing it |
| `is_empty` | Check whether the queue is empty |
| `size` | Return the number of elements in the queue |
| `clear` | Remove all elements from the queue |

------------------------------------------------------------------------------------

## Utility / Output Operations

| Operation | Description |
|---------|-------------|
| `print_queue` | Print queue contents from front to rear |

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines the `ListQueue` class
- Initializes internal list storage
- Exposes public queue methods
- Delegates all logic to `operations.py`
- Contains **no business logic**

### `operations.py`
- Implements all queue behavior
- Enforces FIFO semantics
- Operates directly on the internal list
- Returns explicit, predictable values
- Handles utility output where required

### `main.py`
- Entry point for testing and demonstration
- Validates queue behavior and state transitions
- Intended for fast behavioral verification
- Not designed for production use

------------------------------------------------------------------------------------

## Example Usage

```python
from queue.list_queue.schemas import ListQueue

queue = ListQueue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")

queue.print_queue()
print(queue.dequeue())
print(queue.peek())
print(queue.size())
queue.clear()
```
## Example Output
```python
---------------- Queue -----------------
    Front → | A | B | C | D | ← Rear
----------------------------------------
    Front → A               Rear → D
----------------------------------------

```
---
## Notes

Designed for learning, interviews, and clean architecture practice
- Python lists are not optimal for queue-heavy workloads
- Provided mainly for conceptual clarity and API consistency
- Easily extensible to:
- deque-based queues
- thread-safe queues
- async queues
- priority queues
---
