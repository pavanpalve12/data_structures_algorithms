"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements **operations and invariants** for the Directed Acyclic Graph.

Key responsibility:
- Enforce the **acyclic invariant**
------------------------------------------------------------------------------------
"""

from typing import Any, List

# ------------------------------------------------------------------
# Core Operations
# ------------------------------------------------------------------
def insert_vertex(graph, vertex) -> None:
    """Insert a vertex into the DAG."""
    pass


def insert_edge(graph, from_vertex, to_vertex) -> None:
    """
    Insert a directed edge (u → v).

    Must reject edge if it introduces a cycle.
    """
    pass


def remove_vertex(graph, vertex) -> None:
    """Remove a vertex and all its incident edges."""
    pass


def remove_edge(graph, from_vertex, to_vertex) -> None:
    """Remove a directed edge."""
    pass


# ------------------------------------------------------------------
# DAG Properties
# ------------------------------------------------------------------
def is_dag(graph) -> bool:
    """Return True if graph is acyclic."""
    pass


def topological_sort(graph) -> List[Any]:
    """Return topological ordering of vertices."""
    pass


# ------------------------------------------------------------------
# Traversals
# ------------------------------------------------------------------
def bfs(graph, start_vertex):
    """Breadth-first traversal."""
    pass


def dfs(graph, start_vertex):
    """Depth-first traversal."""
    pass


# ------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------
def print_graph(graph) -> None:
    """Print adjacency list."""
    pass
