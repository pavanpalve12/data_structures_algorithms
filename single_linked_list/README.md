# Singly Linked List (SLL) – Python Implementation

## Overview

This project provides a **modular and fully featured implementation of a Singly
Linked List (SLL)** in Python.

The design prioritizes:
- clean separation of concerns
- readable and maintainable code
- correctness in pointer manipulation
- reusable and testable operations

All list logic is implemented in specialized operation modules, while the
`LinkedList` class serves as a clean public API.

---

## Core Data Structures

### Node
Represents a single element in the list.
- Stores a data value
- Maintains a reference to the next node

### LinkedList
Container class that:
- Manages the head pointer
- Exposes all supported linked list operations
- Delegates logic to operation modules

---

## Functional Categories

### Core Operations

| Function | Description |
|--------|------------|
| `is_empty` | Check whether the list is empty |
| `traverse` | Traverse list and return values and metadata |
| `print_linked_list` | Print the list in forward order |
| `clear` | Remove all nodes from the list |
| `get_length` | Return total number of nodes |

---

### Search Operations

| Function | Description |
|--------|------------|
| `get_last_node` | Return the last node and its previous node |
| `get_node_by_value` | Find a node by its value |
| `get_node_by_index` | Find a node by its index |

---

### Insertion Operations

| Function | Description |
|--------|------------|
| `insert_node_at_head` | Insert a node at the beginning |
| `insert_node_at_end` | Insert a node at the end |
| `insert_node_after_node` | Insert after a target node |
| `insert_node_before_node` | Insert before a target node |
| `insert_node_at_index` | Insert at a specific index |

---

### Removal Operations

| Function | Description |
|--------|------------|
| `remove_node_at_head` | Remove the first node |
| `remove_node_at_end` | Remove the last node |
| `remove_node_by_value` | Remove the first matching value |
| `remove_node_at_index` | Remove node at index |
| `remove_all_nodes` | Remove all nodes |

---

### Utility Operations

| Function | Description |
|--------|------------|
| `reverse_linked_list` | Reverse the list in place |
| `count_node_occurrences` | Count occurrences of a value |
| `find_middle_node` | Find the middle node(s) |
| `find_nth_from_last` | Find nth node from the end |
| `merge_two_linked_lists` | Merge two linked lists |
| `detect_cycle` | Detect a cycle in the list |
| `remove_cycle` | Remove a detected cycle |

---

### Helper Operations

| Function | Description |
|--------|------------|
| `to_list` | Convert list to Python list |
| `from_list` | Build list from Python list |
| `compare_lists` | Compare two lists for equality |
| `clone` | Create a deep copy of the list |
| `remove_duplicates` | Remove duplicate values |
| `get_max` | Return maximum value |
| `get_min` | Return minimum value |
| `print_reverse` | Print list in reverse order |

---

## Design Principles

- Node identity is preserved unless explicitly removed
- Operations manipulate pointers directly
- No unnecessary data copying
- Cycle detection and removal included
- Clear and predictable behavior

---

## Intended Use

This implementation is suitable for:
- learning data structures
- interview preparation
- algorithm practice
- building higher-level abstractions
- debugging pointer-based logic

---

## License

Provided as-is for educational and personal use.
