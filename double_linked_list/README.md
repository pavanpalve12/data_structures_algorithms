# Doubly Linked List (DLL) – Python Implementation
---
## Overview
This project provides a **fully featured, modular implementation of a Doubly Linked List (DLL)** in Python.

The design emphasizes:
- clean separation of concerns
- structural correctness
- explicit APIs
- robust validation utilities

The `DoubleLinkedList` class exposes a rich public interface, while all operational logic is delegated to specialized submodules.
---
## Core Components

### Data Structures

- **Node**  
  Represents a single element in the list, storing:
  - `data`
  - reference to previous node
  - reference to next node

- **DoubleLinkedList**  
  Container that manages:
  - `head` pointer
  - `tail` pointer
  - all list-level operations via wrapper methods

---

## Functional Categories

### Core / Utility Operations

| Function | Description |
|--------|------------|
| `is_empty` | Check whether the list is empty |
| `traverse` | Traverse list and collect structural info |
| `print_linked_list` | Print list in a readable format |
| `clear` | Remove all nodes from the list |

---

### Insertion Operations

| Function | Description |
|--------|------------|
| `insert_at_head` | Insert a node at the beginning |
| `insert_at_tail` | Insert a node at the end |
| `insert_at_index` | Insert a node at a given index |
| `insert_before_node` | Insert before a specific node |
| `insert_after_node` | Insert after a specific node |
| `insert_before_value` | Insert before first matching value |
| `insert_after_value` | Insert after first matching value |
| `insert_sorted_ascending` | Insert while keeping ascending order |
| `insert_sorted_descending` | Insert while keeping descending order |

---

### Deletion Operations

| Function | Description |
|--------|------------|
| `delete_from_head` | Remove the head node |
| `delete_from_tail` | Remove the tail node |
| `delete_at_index` | Remove node at index |
| `delete_node` | Remove a node by reference |
| `delete_by_value` | Remove first node matching value |
| `delete_before_node` | Remove node before a given node |
| `delete_after_node` | Remove node after a given node |
| `delete_all_occurrences` | Remove all nodes matching value |
| `clear` | Remove all nodes |

---

### Traversal Operations

| Function | Description |
|--------|------------|
| `traverse_forward` | Traverse from head to tail |
| `traverse_backward` | Traverse from tail to head |
| `traverse_from_node_forward` | Traverse forward from a node |
| `traverse_from_node_backward` | Traverse backward from a node |

---

### Search Operations

| Function | Description |
|--------|------------|
| `search_by_value` | Find node by value |
| `search_by_index` | Find node by index |
| `search_first_occurrence` | Find first matching value |
| `search_last_occurrence` | Find last matching value |
| `contains` | Check if value exists |
| `get_last_node` | Return the tail node |

---

### Update / Modification Operations

| Function | Description |
|--------|------------|
| `update_node_value` | Update value of a node |
| `update_value_at_position` | Update value at index |
| `replace_all_occurrences` | Replace all matching values |
| `swap_nodes` | Swap two nodes |
| `relink_nodes` | Move a node before another node |

---

### Utility / Information Operations

| Function | Description |
|--------|------------|
| `to_list` | Convert DLL to Python list |
| `from_list` | Build DLL from Python list |
| `get_length` | Return list length |
| `get_middle_node` | Return middle node |
| `get_nth_from_start` | Return nth node from head |
| `get_nth_from_end` | Return nth node from tail |

---

### Reordering / Structural Operations

| Function | Description |
|--------|------------|
| `reverse` | Reverse the list in place |
| `rotate` | Rotate list left or right |
| `split` | Split list at an index |
| `merge` | Merge two lists |

#### Supported merge modes
- **append** → append second list to first
- **alternate** → interleave nodes from both lists

---

### Validation / Integrity Checks

| Function | Description |
|--------|------------|
| `validate_dll_structure` | Run all structural validations |
| `check_forward_backward_consistency` | Verify next/prev symmetry |
| `detect_cycle` | Detect cycles in the list |
| `verify_head_tail_integrity` | Ensure head and tail boundaries |

### Sorting Operations

| Function | Description |
|--------|------------|
| `sort_ascending` | Sort the doubly linked list in ascending order by rearranging node links in-place |
| `sort_descending` | Sort the doubly linked list in descending order by rearranging node links in-place |

---

## Design Principles

- Node identity is preserved unless explicitly deleted
- Structural operations modify links only (no data copying)
- Validation utilities are provided to detect corruption early
- No implicit behavior — all operations are explicit and predictable
- Suitable for learning, debugging, and production-quality usage

---

## Intended Use

This library is ideal for:
- data structure learning and teaching
- interview preparation
- systems programming practice
- building higher-level abstractions on top of linked lists

---

## License

This project is provided as-is for educational and personal use.
