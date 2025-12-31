# Directed Acyclic Graph (DAG) Implementation (Python)

------------------------------------------------------------------------------------

## Overview

This module provides a **Directed Acyclic Graph (DAG)** implementation built on top
of the directed graph abstraction.

A DAG is a directed graph with the additional invariant that:
> **No cycles are allowed**

DAGs are widely used to model:
- Task scheduling
- Dependency resolution
- Build systems
- Workflow pipelines

This implementation focuses on **structure, invariants, and traversal mechanics**,
not algorithmic optimization.

------------------------------------------------------------------------------------

## Key Properties

- Edges are **directed**
- Cycles are **strictly forbidden**
- Graph may have multiple sources and sinks
- Topological ordering is always possible

------------------------------------------------------------------------------------

## Core Operations

| Operation | Description |
|---------|-------------|
| `insert_vertex` | Add a vertex |
| `insert_edge` | Add a directed edge (cycle-safe) |
| `remove_vertex` | Remove vertex and incident edges |
| `remove_edge` | Remove a directed edge |
| `is_dag` | Validate acyclic property |
| `topological_sort` | Linear ordering of vertices |
| `bfs` / `dfs` | Traversals (direction-aware) |

------------------------------------------------------------------------------------

## Architecture

dag/ <br>
└── dag/<br>
    ├── schemas.py      # DAG data container (state only)<br>
    ├── operations.py   # DAG operations and invariants<br>
    ├── main.py         # Test harness<br>
    └── README.md       # Documentation<br>

------------------------------------------------------------------------------------

## Sample Output
### Sample Graph
```text
Sample Graph
A → B → D → F
|    |
↓    ↓
C    E

G → H
```
### Output
```text
---------------------- DAG Structure -----------------------
============= Directed Acyclic Graph =============
	A → ['B', 'C']
	B → ['D', 'E']
	C → []
	D → ['F']
	E → []
	F → []
	G → ['H']
	H → []
==================================================
------------------------------------------------------------
------------------------ Traversals ------------------------
BFS from A : ['A', 'B', 'C', 'D', 'E', 'F']
DFS from A : ['A', 'B', 'D', 'F', 'E', 'C']
------------------------------------------------------------
---------------------- DAG Properties ----------------------
Is DAG                : True
Topological Sort (Kahn): ['A', 'G', 'B', 'C', 'H', 'D', 'E', 'F']
Topological Sort (DFS) : ['A', 'B', 'D', 'F', 'E', 'C']
------------------------------------------------------------
```

------------------------------------------------------------------------------------

## Notes

- DAG extends Directed Graph with a **no-cycle invariant**
- Edge insertion must validate acyclicity
- This serves as a foundation for:
  - Build graphs
  - Job schedulers
  - Dependency analyzers

------------------------------------------------------------------------------------
