# Directed Graph Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular implementation of an Unweighted, Directed Graph**
using an **adjacency list representation**, designed to clearly demonstrate how
directed graph data structures work internally.

The implementation focuses on **core directed graph mechanics**, including:
- vertex and directed-edge insertion and removal
- breadth-first search (BFS) and depth-first search (DFS)
- cycle detection using DFS recursion-stack tracking
- reachability via directed traversal
- clear separation between data representation and behavior

The design follows **production-grade separation of concerns**, isolating:
- data representation (schemas)
- operational logic (operations)
- public-facing API (Graph façade)

This structure is ideal for understanding direction-aware graphs beyond
undirected relationships.

------------------------------------------------------------------------------------

## Architecture

directed_graph/<br>
└── directed_graph/<br>
    ├── schemas.py      # Graph schema (state only, no logic)<br>
    ├── operations.py   # Directed insert/delete, traversal, cycle detection<br>
    └── main.py         # Entry point for testing and experimentation<br>

------------------------------------------------------------------------------------

## Design Philosophy

- **Correctness before optimization**
- **Direction-aware adjacency list**
- **No logic in schema (data) classes**
- **Explicit separation of concerns**
- **Traversal-order independence**
- **Algorithm-first learning approach**

The design mirrors real-world systems such as:
- dependency graphs
- workflow pipelines
- call graphs
- state-transition systems

------------------------------------------------------------------------------------

## Data Structures

### Graph

- Represents a directed graph using an adjacency list
- Conceptually holds:
  - a mapping of vertices to **outgoing neighbors**
- Contains **no traversal or mutation logic**
- Acts as a pure data container

------------------------------------------------------------------------------------

## Core Directed Graph Operations

| Operation | Description |
|---------|-------------|
| `insert_vertex` | Add a vertex to the graph |
| `insert_edge` | Add a directed edge (u → v) |
| `remove_vertex` | Remove a vertex and all incoming/outgoing edges |
| `remove_edge` | Remove a directed edge (u → v) |
| `bfs_iterative` | Iterative breadth-first traversal |
| `bfs_recursive` | Recursive (level-based) BFS |
| `dfs_iterative` | Iterative depth-first traversal |
| `dfs_recursive` | Recursive DFS |
| `detect_cycle` | Detect cycles using DFS recursion stack |
| `print_graph` | Print adjacency list representation |

------------------------------------------------------------------------------------

## Example Directed Graph

```text
A → B → D
↓   ↓
C → D → E
```

Adjacency List:

```text
A → [B, C]
B → [D]
C → [D]
D → [E]
E → []
```

------------------------------------------------------------------------------------

## Graph Properties

### Directionality
- Edges are **one-way**
- Traversal follows **outgoing edges only**
- Reverse traversal requires explicit reverse edges

### Cycles (Directed)
- A cycle exists if DFS encounters a node already in the **current recursion stack**
- Parent-based cycle detection does **not** apply

Example cycle:
```
A → B → C → A
```

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines the `Graph` container
- Holds adjacency list state only
- No traversal, mutation, or validation logic

### `operations.py`
- Implements all directed graph algorithms
- Handles insert/delete operations
- Implements BFS and DFS
- Implements directed cycle detection

### `main.py`
- Entry point for experimentation and learning
- Demonstrates directed graph behavior
- Not intended for production use

------------------------------------------------------------------------------------

## Notes

- Designed for **deep conceptual understanding** of directed graphs
- Emphasizes direction-aware traversal and cycle logic
- Serves as a foundation for:
  - Directed Acyclic Graphs (DAGs)
  - Topological sorting
  - Strongly Connected Components (SCC)
  - Weighted directed graphs

------------------------------------------------------------------------------------
