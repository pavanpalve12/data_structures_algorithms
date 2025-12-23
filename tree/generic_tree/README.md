# Generic Tree Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular implementation of a Generic (N-ary) Tree**
using a **linked, node-based representation**, designed to clearly demonstrate how
tree data structures work internally.

The implementation focuses on **core tree mechanics**, including:
- hierarchical parent–child relationships
- insertion and deletion of nodes
- depth-first and breadth-first traversals
- computation of tree properties (height, depth, size)
- strict invariant enforcement to guarantee correctness

The design mirrors **production-grade separation of concerns** by isolating:
- data representation (schemas)
- structural and traversal logic (operations)
- validation and property computation (helpers)
- public-facing interface (TreeAPI)

This structure is ideal for understanding trees beyond abstract textbook diagrams.

------------------------------------------------------------------------------------

## Architecture

generic_tree/
└── generic_tree/
    ├── schemas.py      # Node and Tree schemas (state only, no logic)
    ├── operations.py   # Insert, delete, search, DFS/BFS traversals
    ├── helpers.py      # Invariants, properties, printing utilities
    ├── tree_api.py     # Public API binding schemas, operations, helpers
    └── main.py         # Entry point for testing and experimentation

------------------------------------------------------------------------------------

## Design Philosophy

- **Correctness before optimization**
- **Explicit parent–child relationships**
- **No logic in schema (data) classes**
- **All behavior delegated to operations layer**
- **Invariant-driven development**
- **Clear public API via TreeAPI facade**

This mirrors how hierarchical structures are modeled in real systems
(file systems, org charts, DOM trees).

------------------------------------------------------------------------------------

## Data Structures

### Node

- Represents a single tree node
- Stores:
  - node data
  - reference to parent node (optional for root)
  - collection of child nodes
- Contains **no traversal or mutation logic**

### Tree

- Thin container holding a reference to the root node
- Does not implement operations directly
- Exists to enforce the concept of a single-rooted structure

------------------------------------------------------------------------------------

## Core Tree Operations

| Operation | Description |
|---------|-------------|
| `insert_node` | Insert a node under a specified parent |
| `delete_node` | Delete a node and its entire subtree |
| `search_node` | Locate a node via traversal |
| `dfs_preorder` | Depth-first traversal (preorder) |
| `dfs_postorder` | Depth-first traversal (postorder) |
| `bfs_traversal` | Breadth-first (level-order) traversal |
| `compute_height` | Compute height of the tree |
| `compute_depth` | Compute depth of a given node |
| `compute_size` | Count total nodes in the tree |

------------------------------------------------------------------------------------

## Tree Invariants (Correctness Rules)

The structure is considered a valid tree only if **all invariants hold**:

- Exactly **one root node**
- Root has `parent = None`
- Every non-root node has **exactly one parent**
- No cycles (a node must never be revisited during traversal)
- All child pointers point **downward only**
- Every node is reachable from the root
- For `n` nodes, there are exactly `n - 1` edges (derived invariant)

Invariant checks are centralized in the helpers module.

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines `Node` and `Tree`
- Holds structural state only
- No traversal, mutation, or validation logic

### `operations.py`
- Implements all structural mutations
- Implements DFS and BFS traversals
- Operates on schema objects
- Contains no public-facing interface

### `helpers.py`
- Computes tree properties (height, depth, size)
- Validates invariants
- Provides tree printing utilities
- Pure, side-effect-free helpers

### `tree_api.py`
- Public-facing API for consumers
- Delegates logic to operations and helpers
- Acts as a facade hiding internal complexity

### `main.py`
- Entry point for testing and learning
- Builds sample trees
- Demonstrates operations and traversals
- Not intended for production use

------------------------------------------------------------------------------------

## Example Usage

```python
from tree_api import TreeAPI

# Create tree with root
tree = TreeAPI("A")

# Build structure
tree.insert_node("B", "A")
tree.insert_node("C", "A")
tree.insert_node("D", "A")

tree.insert_node("E", "B")
tree.insert_node("F", "B")

tree.insert_node("G", "E")
tree.insert_node("H", "E")

tree.insert_node("I", "F")

tree.insert_node("J", "D")
tree.insert_node("K", "D")
tree.insert_node("L", "D")

tree.insert_node("M", "J")
tree.insert_node("N", "J")

# Search
node = tree.search_node("C")
print(node.data)

# Print tree
tree.print_tree()

# Delete a subtree
tree.delete_node("C")

# Traversals
print(tree.dfs_preorder())
print(tree.dfs_postorder())
print(tree.bfs_traversal())

# Tree properties
print(tree.compute_height())
print(tree.compute_height(edges=True))
print(tree.compute_depth("K"))
print(tree.compute_size())
```

------------------------------------------------------------------------------------

## Example Output

```
====================== Tree ======================
Level 0: A → B, C, D
Level 1: B → E, F
Level 1: C → **
Level 1: D → J, K, L
Level 2: E → G, H
Level 2: F → I
Level 2: J → M, N
Level 2: K → **
Level 2: L → **
Level 3: G → **
Level 3: H → **
Level 3: I → **
Level 3: M → **
Level 3: N → **
--------------------------------------------------
Root Node       → A
Size            → 14
Height (Levels) → 4
Height (Edges)  → 3
==================================================

DFS Preorder   : A → B → E → G → H → F → I → D → J → M → N → K → L
DFS Postorder  : G → H → E → I → F → B → M → N → J → K → L → D → A
BFS Traversal  : A → B → D → E → F → J → K → L → G → H → I → M → N
```

------------------------------------------------------------------------------------

## Notes

- Designed for **deep conceptual understanding** of trees
- Emphasizes invariant enforcement and structural correctness
- More verbose than built-in abstractions, but **far more educational**
- Suitable foundation for:
  - binary trees
  - AVL trees
  - red-black trees
  - tries and other hierarchical structures

------------------------------------------------------------------------------------
