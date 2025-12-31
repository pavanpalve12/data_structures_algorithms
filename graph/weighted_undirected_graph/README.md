# Undirected Weighted Graph Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This project provides a **clean, modular implementation of an Undirected, Weighted Graph**
using an **adjacency list representation**, designed to clearly demonstrate how
weighted graph data structures work internally.

The implementation extends the unweighted undirected graph by introducing **edge weights**
while preserving all existing traversal and structural behavior.

The focus areas include:
- weighted edge insertion and update
- vertex and edge deletion
- BFS and DFS traversals (weight-agnostic)
- connected components
- cycle detection
- path cost computation
- shortest path foundations

------------------------------------------------------------------------------------

## Architecture

graph/<br>
└── graph/<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── schemas.py&nbsp;&nbsp;&nbsp;&nbsp;# Graph schema (state only, no logic)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── operations.py&nbsp;# Weighted graph algorithms and operations<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Entry point for testing and experimentation<br>

------------------------------------------------------------------------------------

## Design Philosophy

- **Correctness before optimization**
- **Adjacency-list–driven structure**
- **No logic in schema (data) classes**
- **Explicit separation of concerns**
- **Traversal independent of weights**
- **Algorithm-first learning approach**

------------------------------------------------------------------------------------

## Data Structures

### Graph

- Represents an undirected weighted graph using an adjacency list
- Each vertex maps to a list of `(neighbor, weight)` tuples
- Stores **state only**
- Delegates all behavior to `operations.py`

------------------------------------------------------------------------------------

## Core Graph Operations

| Operation | Description |
|---------|-------------|
| `insert_vertex` | Add a vertex to the graph |
| `insert_edge(u, v, w)` | Add or update weighted edge `u ↔ v` |
| `update_edge_weight` | Update weight of an existing edge |
| `remove_vertex` | Remove a vertex and all incident edges |
| `remove_edge` | Remove an undirected weighted edge |
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
        A
      / | \
     B  C  D
     |     |
     D-----+
```

Adjacency List:

```text
Graph [A] → [(B, 4), (C, 2), (D, 1)]
Graph [B] → [(A, 4), (D, 5)]
Graph [C] → [(A, 2), (D, 3)]
Graph [D] → [(A, 1), (B, 5), (C, 3)]
```

------------------------------------------------------------------------------------

## Shortest Path & Cost Analysis

### Path Cost

- Path cost is the **sum of weights** along a given vertex path
- Each consecutive edge in the path must exist
- Invalid paths are rejected

Example:
```
Path: A → D → C
Cost: 1 + 3 = 4
```

### Shortest Path (Foundational)

- Shortest path identifies the **minimum total weight** between vertices
- Traversal order alone is insufficient
- Requires weight-aware algorithms (e.g., Dijkstra)

------------------------------------------------------------------------------------

## Sample Output Representation
### Sample Graph
```text
         A
       / | \
     4/  |  \2
     B  1|   C
      \  |  /
      5\ | /3
         D

        E — F
```
### Sample Output
```text
----------------- Weighted Graph Structure -----------------
=========== Undirected Weighted Graph ============
	Graph [A] → [('B', 4), ('C', 2), ('D', 1)]
	Graph [B] → [('A', 4), ('D', 5)]
	Graph [C] → [('A', 2), ('D', 3)]
	Graph [D] → [('B', 5), ('C', 3), ('A', 1)]
	Graph [E] → [('F', 7)]
	Graph [F] → [('E', 7)]
==================================================
------------------------------------------------------------
--------------- Traversals (Weights Ignored) ---------------
BFS (Iterative) from A : ['A', 'B', 'C', 'D']
BFS (Recursive) from A : ['A', 'B', 'C', 'D']
DFS (Iterative) from A : ['A', 'D', 'C', 'B']
DFS (Recursive) from A : ['A', 'B', 'D', 'C']
------------------------------------------------------------
--------------------- Graph Properties ---------------------
Connected Components : 2
Cycle Detected       : True
------------------------------------------------------------
--------------------- Path Cost Tests ----------------------
Path           : ['A', 'D', 'C']
Total Cost     : 4
------------------------------------------------------------
----------------- Shortest Path (Dijkstra) -----------------
Distances from A : {'A': 0, 'B': 4, 'C': 2, 'D': 1, 'E': inf, 'F': inf}
Shortest Path A → D : ['A', 'B']
------------------------------------------------------------
```

------------------------------------------------------------------------------------

## Module Responsibilities

### `schemas.py`
- Defines the `Graph` container
- Holds adjacency list state only

### `operations.py`
- Implements weighted graph operations
- Traversals (weight-agnostic)
- Cycle detection
- Path cost computation
- Shortest path foundations

### `main.py`
- Entry point for experimentation and learning

------------------------------------------------------------------------------------

## Notes

- Designed for **deep conceptual understanding** of weighted graphs
- Builds directly on the unweighted graph implementation
- Foundation for shortest-path and optimization algorithms

------------------------------------------------------------------------------------
