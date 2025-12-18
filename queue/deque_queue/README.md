# Deque-Based Queue Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular Queue implementation backed by
`collections.deque`**, designed with a strict separation of concerns.

The implementation follows **FIFO (First-In-First-Out)** semantics and mirrors
production-grade design principles by isolating:
- public interface (schemas)
- operational logic (operations)
- execution / validation (main)

This structure makes the queue easy to understand, test, extend, and swap with
other implementations (e.g., list-based queue) without changing client code.

------------------------------------------------------------------------------------

## Architecture

queue/
└── deque_queue/
├── schemas.py # Public Queue interface (no logic)
├── operations.py # Queue behavior & business logic
└── main.py # Entry point for testing and demonstration

---

------------------------------------------------------------------------------------

## Design Philosophy

- **FIFO correctness first**
- **No logic in container classes**
- **All behavior delegated to operations layer**
- **Internal state managed via a single deque**
- **Readable, predictable, and testable design**

This mirrors how real-world libraries separate interface from implementation.

------------------------------------------------------------------------------------

## Data Structure

### DequeQueue

- Queue abstraction implemented using `collections.deque`
- Provides O(1) enqueue and dequeue operations
- Maintains internal state via a protected deque attribute

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
- Defines the `DequeQueue` class
- Initializes internal deque storage
- Exposes public queue methods
- Delegates all logic to `operations.py`
- Contains **no business logic**

### `operations.py`
- Implements all queue behavior
- Enforces FIFO semantics
- Operates directly on the internal deque
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
from queue.deque_queue.schemas import DequeQueue

queue = DequeQueue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

queue.print_queue()
print(queue.dequeue())
print(queue.peek())
print(queue.size())
queue.clear()

```
---
## Example Output
```python
---------------- Queue -----------------
    Front → | A | B | C | D | ← Rear
----------------------------------------
    Front → A               Rear → D
----------------------------------------
```
---
### Notes
- Designed for learning, interviews, and clean architecture practice
- collections.deque is preferred over list for queues in Python
- Exception handling is intentionally minimal

Easily extensible to:
- thread-safe queues
- async queues

priority queues
---