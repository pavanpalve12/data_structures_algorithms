# Graph Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular implementation of an Unweighted, Undirected Graph**
using an **adjacency list representation**, designed to clearly demonstrate how
graph data structures work internally.

The implementation focuses on **core graph mechanics**, including:
- vertex and edge insertion (explicit and edge-driven)
- vertex and edge deletion
- breadth-first search (BFS) and depth-first search (DFS)
- connected components discovery
- cycle detection in undirected graphs
- graph connectivity analysis

The design follows **production-grade separation of concerns**, isolating:
- data representation (schemas)
- operational logic (operations)

This structure is ideal for understanding graphs beyond abstract diagrams and textbook definitions.

------------------------------------------------------------------------------------

## Architecture

graph/<br>
└── graph/<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── schemas.py&nbsp;&nbsp;&nbsp;&nbsp;# Graph schema (state only, no logic)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── operations.py&nbsp;# Insert, delete, traversal, graph algorithms<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Entry point for testing and experimentation<br>

------------------------------------------------------------------------------------

## Design Philosophy

- **Correctness before optimization**
- **Adjacency-list–driven structure**
- **No logic in schema (data) classes**
- **Explicit separation of concerns**
- **Traversal-order independence**
- **Algorithm-first learning approach**

The design mirrors how graphs are implemented in real systems such as:
- dependency resolvers
- workflow engines (DAGs)
- network topology models
- traversal-based problem solvers

------------------------------------------------------------------------------------

## Data Structures

### Graph

- Represents an undirected graph using an adjacency list
- Conceptually holds:
  - a mapping of vertices to neighboring vertices
- Contains **no traversal or mutation logic**
- Acts as a pure data container

------------------------------------------------------------------------------------

## Core Graph Operations

| Operation | Description |
|---------|-------------|
| `insert_vertex` | Add a vertex to the graph |
| `insert_edge` | Add an undirected edge (edge-driven insert supported) |
| `remove_vertex` | Remove a vertex and all incident edges |
| `remove_edge` | Remove an undirected edge |
| `bfs_iterative` | Iterative breadth-first traversal |
| `bfs_recursive` | Recursive (level-based) BFS |
| `dfs_iterative` | Iterative depth-first traversal |
| `dfs_recursive` | Recursive DFS |
| `get_connected_components` | Count connected components |
| `detect_cycle` | Detect cycles using DFS with parent tracking |
| `print_graph` | Print adjacency list representation |

------------------------------------------------------------------------------------

## Example Graph

```text
        A — B — C
        |   |
        E — D

        F — G
```

Adjacency List:

```text
================ Undirected Graph ================
	Graph [A] → [B, E]
	Graph [B] → [A, C, D]
	Graph [C] → [B]
	Graph [D] → [B, E]
	Graph [E] → [D, A]
	Graph [F] → [G]
	Graph [G] → [F]
==================================================
------------------------ Traversals ------------------------
BFS (Iterative) from A : ['A', 'B', 'E', 'C', 'D']
BFS (Recursive) from A : ['A', 'B', 'E', 'C', 'D']
DFS (Iterative) from A : ['A', 'E', 'D', 'B', 'C']
DFS (Recursive) from A : ['A', 'B', 'C', 'D', 'E']
------------------------------------------------------------
--------------------- Graph Properties ---------------------
Connected Components        : 2
Cycle Detected (Iterative)  : True
Cycle Detected (Recursive)  : True
------------------------------------------------------------
```

------------------------------------------------------------------------------------

## Graph Properties

### Connected Components
- A connected component is a maximal set of vertices reachable from one another
- Graphs may have one or more connected components

### Graph Connectivity
- A graph is **connected** if it has exactly one connected component
- A graph is **disconnected** if it has more than one connected component

### Cycles
- A cycle exists if traversal returns to an already visited vertex
  that is **not the parent** in DFS
- Cycle detection uses DFS with parent tracking

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines the `Graph` data container
- Holds adjacency list state only
- No traversal, mutation, or validation logic

### `operations.py`
- Implements all graph algorithms
- Handles insert/delete operations
- Implements BFS and DFS (iterative and recursive)
- Computes connected components
- Detects cycles in undirected graphs

### `main.py`
- Entry point for experimentation and learning
- Demonstrates graph operations
- Not intended for production use

------------------------------------------------------------------------------------

## Notes

- Designed for **deep conceptual understanding** of graphs
- Emphasizes traversal logic and structural correctness
- Intentionally explicit and step-driven for learning
- Serves as a strong foundation for:
  - Directed graphs
  - DAGs
  - Weighted graphs
  - Advanced graph algorithms

------------------------------------------------------------------------------------
