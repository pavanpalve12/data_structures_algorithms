
# Binary Tree Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular implementation of a Normal Binary Tree**
using a **linked, node-based representation**, designed to clearly demonstrate how
binary tree data structures work internally.

The implementation focuses on **core binary tree mechanics**, including:
- level-order (BFS) based insertion
- deletion using deepest-rightmost replacement
- depth-first and breadth-first traversals
- computation of tree properties (height, depth, size)
- strict invariant enforcement to guarantee correctness

The design follows **production-grade separation of concerns**, isolating:
- data representation (schemas)
- operational logic (operations)
- reusable mechanics (helpers)
- invariant validation (invariant)
- public-facing interface (TreeAPI)

This structure is ideal for understanding binary trees beyond abstract diagrams.

------------------------------------------------------------------------------------

## Architecture

binary_tree/<br>
└── binary_tree/<br>
    ├── schemas.py      # Node and Tree schemas (state only, no logic)<br>
    ├── operations.py   # Insert, delete, search, DFS/BFS orchestration<br>
    ├── helpers.py      # BFS helpers, traversal helpers, printing utilities<br>
    ├── invariant.py    # Tree invariant validation logic<br>
    ├── tree_api.py     # Public API facade<br>
    └── main.py         # Entry point for testing and experimentation<br>

------------------------------------------------------------------------------------

## Design Philosophy

- **Correctness before optimization**
- **Level-order driven structure**
- **No logic in schema (data) classes**
- **Explicit separation of concerns**
- **Invariant-driven development**
- **Thin public API via TreeAPI**

The design mirrors how binary trees are implemented in real systems
(memory heaps, schedulers, indexing structures).

------------------------------------------------------------------------------------

## Data Structures

### Node

- Represents a single binary tree node
- Conceptually holds:
  - node value
  - left child reference
  - right child reference
- Contains **no traversal or mutation logic**

### Tree

- Thin container holding a reference to the root node
- Enforces the concept of a single-rooted structure
- Does not implement operations directly

------------------------------------------------------------------------------------

## Core Binary Tree Operations

| Operation | Description |
|---------|-------------|
| `insert_node` | Insert a node using level-order (left-to-right) insertion |
| `delete_node` | Delete a node using deepest-rightmost replacement |
| `search_node` | Locate a node using BFS traversal |
| `dfs_preorder` | Preorder depth-first traversal |
| `dfs_inorder` | Inorder depth-first traversal |
| `dfs_postorder` | Postorder depth-first traversal |
| `bfs_level_order` | Level-order (BFS) traversal |
| `compute_height` | Compute height of the tree (levels or edges) |
| `compute_depth` | Compute depth of a given node |
| `compute_size` | Count total nodes in the tree |
| `print_tree` | Print tree structure with parent–child relationships |

------------------------------------------------------------------------------------
## Sample Output
```text
====================== Tree ======================
	Level 0: A → B, C
	Level 1: B → D, E
	Level 1: C → F, **
	Level 2: D → **
	Level 2: E → **
	Level 2: F → **
--------------------------------------------------
	Note:
	 - Parent → Children
	 - leaf node → **
--------------------------------------------------
	Root Node       → A
	Size            → 6
	Height (Levels) → 3
	Height (Edges)  → 2
==================================================
```

## Tree Invariants (Correctness Rules)

The structure is considered a valid **normal binary tree** only if all invariants hold:

- Exactly **one root node**
- Root is the only node with no parent
- Every non-root node has **exactly one parent**
- Each node has **at most two children** (left and right)
- Partial nodes may have **left OR right child**
- All nodes are reachable from the root
- For `n` nodes, there are exactly `n - 1` edges
- Acyclicity is implied by connectivity and edge count
- Left-first insertion is a **policy**, not an invariant

Invariant validation is centralized in the `invariant` module.

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines `Node` and `Tree`
- Holds structural state only
- No traversal, mutation, or validation logic

### `operations.py`
- Coordinates insert, delete, search operations
- Orchestrates DFS and BFS traversals
- Delegates mechanics to helpers
- Contains no helper implementations

### `helpers.py`
- Implements BFS slot finding
- Implements deepest-rightmost node discovery
- Implements traversal helpers
- Implements tree printing utilities
- Contains reusable, side-effect-free helpers

### `invariant.py`
- Validates tree correctness
- Builds parent maps using BFS
- Verifies connectivity, edge count, and structure
- Read-only validation logic only

### `tree_api.py`
- Public-facing API for consumers
- Delegates all behavior to operations/helpers
- Acts as a facade hiding internal complexity

### `main.py`
- Entry point for experimentation and learning
- Demonstrates tree operations
- Not intended for production use

------------------------------------------------------------------------------------

## Notes

- Designed for **deep conceptual understanding** of binary trees
- Emphasizes invariant enforcement and structural correctness
- Intentionally verbose and explicit for learning purposes
- Serves as a strong foundation for:
  - Binary Search Trees (BST)
  - Heaps
  - AVL Trees
  - Red-Black Trees

------------------------------------------------------------------------------------
