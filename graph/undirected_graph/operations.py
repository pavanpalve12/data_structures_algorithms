"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements the **behavior and algorithms** for the Graph data structure.

It contains all mutation logic, traversal algorithms, and graph property computations
that operate on the core Graph schema defined in `schemas.py`.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement vertex and edge insert/remove operations
- Implement BFS and DFS (iterative and recursive)
- Implement connected components logic
- Implement cycle detection for undirected graphs

------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- insert_vertex
- insert_edge
- remove_vertex
- remove_edge
- bfs_iterative
- bfs_recursive
- dfs_iterative
- dfs_recursive
- get_connected_components
- detect_cycle_iterative
- detect_cycle_recursive
- print_graph

------------------------------------------------------------------------------------
Dependencies
------------------------------------------------------------------------------------
- schemas.Graph

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All functions operate on the adjacency-list dictionary (`Graph.graph`)
  passed explicitly from the Graph container
- Graph schema is treated as a data container only
- Traversal order is not guaranteed or enforced
- No I/O or persistence logic exists in this module
------------------------------------------------------------------------------------
"""

from collections import deque
from typing import Any, List

from schemas import Graph


# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
def insert_vertex(graph: Graph, vertex: Any) -> None:
    """
    Add a vertex to the graph.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Unique vertex identifier
    :return: None
    """
    if not _vertex_exists(graph, vertex):
        graph[vertex] = []


def insert_edge(graph: Graph, from_vertex: Any, to_vertex: Any) -> None:
    """
    Add an undirected edge between two vertices.

    Missing vertices may be auto-created.

    :param graph: Adjacency list (Graph.graph)
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: None
    """
    if not _vertex_exists(graph, from_vertex):
        graph[from_vertex] = []

    if not _vertex_exists(graph, to_vertex):
        graph[to_vertex] = []

    if not _edge_exists(graph, from_vertex, to_vertex):
        graph[from_vertex].append(to_vertex)

    if not _edge_exists(graph, to_vertex, from_vertex):
        graph[to_vertex].append(from_vertex)


def remove_vertex(graph: Graph, vertex: Any) -> None:
    """
    Remove a vertex and all its incident edges from the graph.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Vertex to remove
    :return: None
    """
    neighbors = list(graph[vertex])  # FIX: safe copy

    for neighbor in neighbors:
        if _edge_exists(graph, neighbor, vertex):
            graph[neighbor].remove(vertex)

    del graph[vertex]


def remove_edge(graph: Graph, from_vertex: Any, to_vertex: Any) -> None:
    """
    Remove an undirected edge between two vertices.

    :param graph: Adjacency list (Graph.graph)
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
    :return: None
    """
    if from_vertex in graph and to_vertex in graph[from_vertex]:
        graph[from_vertex].remove(to_vertex)

    if to_vertex in graph and from_vertex in graph[to_vertex]:
        graph[to_vertex].remove(from_vertex)


# ----------------------------------------------------------------------
# BFS Traversal
# ----------------------------------------------------------------------
def bfs_iterative(graph: Graph, start_vertex: Any) -> List[Any]:
    """
    Perform iterative Breadth-First Search (BFS).

    :param graph: Adjacency list (Graph.graph)
    :param start_vertex: Starting vertex
    :return: BFS traversal order
    """
    visited = []
    neighbor_queue = deque()
    current = start_vertex

    while True:
        if current not in visited:
            visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in neighbor_queue:
                neighbor_queue.append(neighbor)

        if not neighbor_queue:
            break

        current = neighbor_queue.popleft()

    return visited


def bfs_recursive(
        graph: Graph,
        level_vertices: List[Any],
        visited: List[Any]
) -> List[Any]:
    """
    Perform recursive (level-based) Breadth-First Search (BFS).

    :param graph: Adjacency list (Graph.graph)
    :param level_vertices: Current BFS frontier
    :param visited: List of visited vertices
    :return: BFS traversal order
    """
    if not level_vertices:
        return visited

    next_level = []

    for vertex in level_vertices:
        if vertex not in visited:
            visited.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                next_level.append(neighbor)

    return bfs_recursive(graph, next_level, visited)


# ----------------------------------------------------------------------
# DFS Traversals
# ----------------------------------------------------------------------
def dfs_iterative(graph: Graph, start_vertex: Any) -> List[Any]:
    """
    Perform iterative Depth-First Search (DFS).

    :param graph: Adjacency list (Graph.graph)
    :param start_vertex: Starting vertex
    :return: DFS traversal order
    """
    visited = []
    neighbor_stack = []
    current = start_vertex

    while True:
        if current not in visited:
            visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in neighbor_stack:
                neighbor_stack.append(neighbor)

        if not neighbor_stack:
            break

        current = neighbor_stack.pop()

    return visited


def dfs_recursive(
        graph: Graph,
        vertex: Any,
        visited: List[Any]
) -> List[Any]:
    """
    Perform recursive Depth-First Search (DFS).

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Current vertex
    :param visited: List of visited vertices
    :return: DFS traversal order
    """
    if vertex is None:
        return visited

    visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


# ----------------------------------------------------------------------
# Graph State Operations
# ----------------------------------------------------------------------
def get_connected_components(graph: Graph) -> int:
    """
    Compute the number of connected components in the graph.

    :param graph: Adjacency list (Graph.graph)
    :return: Number of connected components
    """
    all_vertices = graph.keys()
    covered = list(all_vertices)
    connected_count = 0

    while covered:
        visited = bfs_recursive(graph, [covered[0]], [])

        for vertex in visited:
            covered.remove(vertex)

        connected_count += 1

    return connected_count


def detect_cycle_iterative(graph: Graph, start_vertex: Any) -> bool:
    """
    Detect whether the graph contains a cycle using iterative DFS.

    :param graph: Adjacency list (Graph.graph)
    :param start_vertex: Starting vertex
    :return: True if a cycle exists, otherwise False
    """
    visited = []
    stack = [(start_vertex, None)]

    while stack:
        current, parent = stack.pop()

        if current not in visited:
            visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append((neighbor, current))
            elif neighbor != parent:
                return True

    return False


def detect_cycle_recursive(
        graph: Graph,
        vertex: Any,
        parent: Any = None,
        visited: List[Any] = None
) -> bool:
    """
    Detect whether the graph contains a cycle using recursive DFS.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Current vertex
    :param parent: Parent vertex in DFS tree
    :param visited: List of visited vertices
    :return: True if a cycle exists, otherwise False
    """
    if visited is None:
        visited = []

    if vertex is None:
        return False

    visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if detect_cycle_recursive(graph, neighbor, vertex, visited):
                return True
        elif neighbor != parent:
            return True

    return False


# ----------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------
def print_graph(graph: Graph) -> None:
    """
    Print the adjacency list representation of the graph.

    :param graph: Adjacency list (Graph.graph)
    :return: None
    """
    width = 50
    title = " Undirected Graph "
    header = title.center(width, '=')
    footer = "=" * width

    print(header)
    for vertex, neighbors in graph.items():
        print(f"\tGraph [{vertex}] → [{', '.join([str(n) for n in neighbors])}]")
    print(footer)


# ----------------------------------------------------------------------
# Internal Helpers
# ----------------------------------------------------------------------
def _vertex_exists(graph: Graph, vertex: Any) -> bool:
    """
    Check if a vertex exists in the graph.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Vertex identifier
    :return: True if vertex exists, otherwise False
    """
    return vertex in graph


def _edge_exists(graph: Graph, from_vertex: Any, to_vertex: Any) -> bool:
    """
    Check if an edge exists in the graph.

    :param graph: Adjacency list (Graph.graph)
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: True if edge exists, otherwise False
    """
    return to_vertex in graph[from_vertex]
