# Tree Implementations in Python

This document provides a **unified overview of Tree data structure implementations**
available in this repository.

The goal is to demonstrate how **different tree variants** share a common hierarchical
foundation while differing in **structural constraints, invariants, and operations**.

Currently covered implementations:
1. **Generic (N-ary) Tree**
2. **Binary Tree**
3. **Binary Search Tree (BST)**

---

## Tree Concept (Quick Recap)

A **tree** is a hierarchical, non-linear data structure consisting of:
- **Nodes** (data elements)
- **Edges** (parent–child relationships)

Key properties:
- Exactly **one root**
- No cycles
- All nodes are reachable from the root

Trees are widely used in:
- file systems
- organizational hierarchies
- parsers and ASTs
- indexing and search systems

---

## Core Tree Operations (Common Across Variants)

| Operation | Description |
|---------|-------------|
| `insert_node` | Insert a node into the tree |
| `delete_node` | Delete a node (and subtree if applicable) |
| `search_node` | Locate a node |
| `dfs_traversal` | Depth-first traversal |
| `bfs_traversal` | Breadth-first traversal |
| `compute_height` | Compute tree height |
| `compute_depth` | Compute node depth |
| `compute_size` | Count total nodes |
| `print_tree` | Visualize tree structure |

---

## Implementation 1: Generic (N-ary) Tree

### Characteristics
- Each node can have **any number of children**
- Explicit parent–child relationships
- No ordering constraints

### Supported Operations
- Insert node under any parent
- Delete subtree
- DFS (pre/post order)
- BFS traversal
- Height, depth, size computation
- Invariant validation

---
## Sample Output Representation
```text
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
Note:
 - Parent → Children
 - leaf node → **
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

---

## Implementation 2: Binary Tree

### Characteristics
- Each node has **at most two children** (left, right)
- No ordering constraint on node values
- Level-order insertion policy

### Supported Operations
- Level-order insertion
- Deepest-rightmost deletion
- DFS (pre/in/post order)
- BFS traversal
- Height, depth, size computation
- Invariant validation

---
## Sample Output Representation
```text
================== Binary Tree ===================
	Level 0: A → B, C
	Level 1: B → D, E
	Level 1: C → F, G
	Level 2: D → H
	Level 2: E → **
	Level 2: F → **
	Level 2: G → **
	Level 3: H → **
--------------------------------------------------
	Legend: 
	 - Parent → Children Relationship
	 - **     → Leaf node
--------------------------------------------------
	Root Node       → A
	Size            → 8
	Height (Levels) → 4
	Height (Edges)  → 3
	Edges           → 7
==================================================
```

---

## Implementation 3: Binary Search Tree (BST)

### Characteristics
- Binary tree with **ordering invariant**
- Left subtree < Node < Right subtree
- Enables efficient search operations

### Supported Operations
- Ordered insertion
- Ordered deletion
- Search (O(h))
- DFS (inorder yields sorted output)
- BFS traversal
- Height, depth, size computation

---
## Sample Output Representation
## Sample Output

```text
================== Binary Search Tree ==================
    Level 0: 15 → 10, 20
    Level 1: 10 → 8, 12
    Level 1: 20 → 18, 25
    Level 2: 12 → 11, 13
    Level 2: 25 → 22, 27
--------------------------------------------------------
    Root Node       → 15
    Size            → 11
    Height (Levels) → 4
    Height (Edges)  → 3
========================================================

DFS Inorder   : 8 → 10 → 11 → 12 → 13 → 15 → 18 → 20 → 22 → 25 → 27
DFS Preorder  : 15 → 10 → 8 → 12 → 11 → 13 → 20 → 18 → 25 → 22 → 27
DFS Postorder : 8 → 11 → 13 → 12 → 10 → 18 → 22 → 27 → 25 → 20 → 15
```

---

## Architectural Design (Common)

All tree implementations follow a consistent architecture:

```
tree/<variant>/
├── schemas.py      # Node / Tree schemas (state only)
├── operations.py   # Insert, delete, traversal logic
├── helpers.py      # Properties, printing, invariants
├── tree_api.py     # Public API facade
└── main.py         # Test harness
```

### Design Principles
- No logic in schema classes
- Invariant-driven correctness
- Clear separation of concerns
- Educational, explicit implementations

---

## Summary Comparison

| Aspect | Generic Tree | Binary Tree | BST |
|------|--------------|-------------|-----|
| Max Children | Unlimited | 2 | 2 |
| Ordering | None | None | Enforced |
| Search Efficiency | O(n) | O(n) | O(log n) avg |
| Invariants | Parent-child | Structural | Structural + ordering |

---

## Future Extensions

- AVL Trees
- Red-Black Trees
- Heaps
- Tries

---

## Final Notes

The **tree abstraction remains constant** across implementations.
Each variant adds **constraints and invariants** to serve specific use cases.

This layered approach allows incremental learning and clean extensibility.
