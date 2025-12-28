# Binary Search Tree (BST) Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular implementation of a Binary Search Tree (BST)**
built on top of a binary tree structure, designed to demonstrate how **ordered trees**
enable efficient searching and sorting.

The implementation focuses on:
- ordered insertion and deletion
- efficient search operations
- depth-first and breadth-first traversals
- strict invariant enforcement

------------------------------------------------------------------------------------

## BST Property (Core Invariant)

For every node:
- Values in the **left subtree** are strictly less than the node
- Values in the **right subtree** are greater than or equal to the node

This invariant enables logarithmic-time operations on average.

------------------------------------------------------------------------------------

## Core BST Operations

| Operation | Description |
|---------|-------------|
| `insert_node` | Insert node following BST ordering |
| `delete_node` | Delete node while preserving ordering |
| `search_node` | Locate a value efficiently |
| `dfs_inorder` | Inorder traversal (sorted output) |
| `dfs_preorder` | Preorder traversal |
| `dfs_postorder` | Postorder traversal |
| `bfs_level_order` | Level-order traversal |
| `compute_height` | Compute height |
| `compute_depth` | Compute depth |
| `compute_size` | Count nodes |
| `print_tree` | Visualize structure |

------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------

## Notes

- BST builds on binary tree mechanics
- Inorder traversal yields sorted sequence
- Performance depends on tree balance
- Forms the foundation for AVL and Red-Black Trees

------------------------------------------------------------------------------------
