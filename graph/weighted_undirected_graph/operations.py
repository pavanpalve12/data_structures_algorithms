"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements the **behavior and algorithms** for the Undirected Weighted
Graph data structure.

It reuses all structure-only logic from the unweighted graph implementation and
defines extension points for weight-aware algorithms such as shortest path
computation.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement vertex and edge insert/remove operations
- Implement BFS and DFS (iterative and recursive)
- Implement connected components logic
- Implement cycle detection for undirected graphs
- Define interfaces for weight-aware algorithms

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All functions operate on adjacency-list dictionary (`Graph.graph`)
- Adjacency list format: vertex -> List[(neighbor, weight)]
- Traversals ignore weights
- Graph schema is treated as a data container only
------------------------------------------------------------------------------------
"""

from collections import deque
from typing import Any, List


# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
def insert_vertex(graph, vertex: Any) -> None:
    """
    Add a vertex to the graph if it does not already exist.

    :param graph: Adjacency list representation of the graph
    :param vertex: Vertex identifier
    :return: None
    """
    if vertex not in graph:
        graph[vertex] = []


def insert_edge(graph, from_vertex: Any, to_vertex: Any, weight: Any) -> None:
    """
    Add or update an undirected weighted edge between two vertices.

    If the edge already exists, its weight may be updated.
    If one or both vertices do not exist, they may be created.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
    :param weight: Weight associated with the edge
    :return: None
    """
    pass


def update_edge_weight(graph, from_vertex: Any, to_vertex: Any, weight: Any) -> None:
    """
    Update the weight of an existing undirected edge.

    If the edge does not exist, the behavior is implementation-defined
    (e.g., no-op or edge creation).

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
    :param weight: New weight to apply
    :return: None
    """
    pass


def get_edge_weight(graph, from_vertex: Any, to_vertex: Any):
    """
    Retrieve the weight associated with an undirected edge.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
    :return: Weight of the edge if it exists, otherwise None
    """
    pass


def remove_vertex(graph, vertex: Any) -> None:
    """
    Remove a vertex and all its incident edges from the graph.

    :param graph: Adjacency list representation of the graph
    :param vertex: Vertex to remove
    :return: None
    """
    if vertex not in graph:
        return

    neighbors = list(graph[vertex])

    for neighbor, _ in neighbors:
        graph[neighbor] = [
            (n, w) for n, w in graph[neighbor] if n != vertex
        ]

    del graph[vertex]


def remove_edge(graph, from_vertex: Any, to_vertex: Any) -> None:
    """
    Remove an undirected edge between two vertices.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
    :return: None
    """
    if from_vertex in graph:
        graph[from_vertex] = [
            (n, w) for n, w in graph[from_vertex] if n != to_vertex
        ]

    if to_vertex in graph:
        graph[to_vertex] = [
            (n, w) for n, w in graph[to_vertex] if n != from_vertex
        ]


# ----------------------------------------------------------------------
# BFS Traversal (weight-agnostic)
# ----------------------------------------------------------------------
def bfs_iterative(graph, start_vertex: Any) -> List[Any]:
    """
    Perform iterative Breadth-First Search (BFS).

    Traversal order is based on graph structure only;
    edge weights are ignored.

    :param graph: Adjacency list representation of the graph
    :param start_vertex: Starting vertex
    :return: BFS traversal order
    """
    visited = []
    neighbor_queue = deque()
    current = start_vertex

    while True:
        if current not in visited:
            visited.append(current)

        for neighbor, _ in graph[current]:
            if neighbor not in visited and neighbor not in neighbor_queue:
                neighbor_queue.append(neighbor)

        if not neighbor_queue:
            break

        current = neighbor_queue.popleft()

    return visited


def bfs_recursive(graph, level_vertices: List[Any], visited: List[Any]) -> List[Any]:
    """
    Perform recursive (level-based) Breadth-First Search (BFS).

    :param graph: Adjacency list representation of the graph
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

        for neighbor, _ in graph[vertex]:
            if neighbor not in visited:
                next_level.append(neighbor)

    return bfs_recursive(graph, next_level, visited)


# ----------------------------------------------------------------------
# DFS Traversals (weight-agnostic)
# ----------------------------------------------------------------------
def dfs_iterative(graph, start_vertex: Any) -> List[Any]:
    """
    Perform iterative Depth-First Search (DFS).

    Traversal order is based on graph structure only;
    edge weights are ignored.

    :param graph: Adjacency list representation of the graph
    :param start_vertex: Starting vertex
    :return: DFS traversal order
    """
    visited = []
    neighbor_stack = []
    current = start_vertex

    while True:
        if current not in visited:
            visited.append(current)

        for neighbor, _ in graph[current]:
            if neighbor not in visited and neighbor not in neighbor_stack:
                neighbor_stack.append(neighbor)

        if not neighbor_stack:
            break

        current = neighbor_stack.pop()

    return visited


def dfs_recursive(graph, vertex: Any, visited: List[Any]) -> List[Any]:
    """
    Perform recursive Depth-First Search (DFS).

    :param graph: Adjacency list representation of the graph
    :param vertex: Current vertex
    :param visited: List of visited vertices
    :return: DFS traversal order
    """
    if vertex is None:
        return visited

    visited.append(vertex)

    for neighbor, _ in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


# ----------------------------------------------------------------------
# Graph State Operations
# ----------------------------------------------------------------------
def get_connected_components(graph) -> int:
    """
    Compute the number of connected components in the graph.

    :param graph: Adjacency list representation of the graph
    :return: Number of connected components
    """
    covered = list(graph.keys())
    connected_count = 0

    while covered:
        visited = bfs_recursive(graph, [covered[0]], [])

        for vertex in visited:
            covered.remove(vertex)

        connected_count += 1

    return connected_count


def detect_cycle(graph, start_vertex: Any) -> bool:
    """
    Detect whether the undirected graph contains a cycle.

    Uses DFS with parent tracking.

    :param graph: Adjacency list representation of the graph
    :param start_vertex: Starting vertex
    :return: True if a cycle exists, otherwise False
    """
    visited = []
    stack = [(start_vertex, None)]

    while stack:
        current, parent = stack.pop()

        if current not in visited:
            visited.append(current)

        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                stack.append((neighbor, current))
            elif neighbor != parent:
                return True

    return False


# ----------------------------------------------------------------------
# Weight-Aware Algorithms
# ----------------------------------------------------------------------
def get_path_cost(graph, path: List[Any]):
    """
    Compute the total cost of a given vertex path.

    Validates that each consecutive edge in the path exists
    before accumulating its weight.

    :param graph: Adjacency list representation of the graph
    :param path: List of vertices representing a path
    :return: Total cost of the path, or None if path is invalid
    """
    pass


def shortest_path_dijkstra(graph, source: Any):
    """
    Compute the shortest path distances from a source vertex
    to all other vertices using Dijkstra's algorithm.

    :param graph: Adjacency list representation of the graph
    :param source: Source vertex
    :return: Mapping of vertex -> shortest distance
    """
    pass


def shortest_path_to(graph, source: Any, destination: Any):
    """
    Compute the shortest path and total cost between two vertices.

    :param graph: Adjacency list representation of the graph
    :param source: Source vertex
    :param destination: Destination vertex
    :return: Path and total cost
    """
    pass


# ----------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------
def print_graph(graph) -> None:
    """
    Print the adjacency list representation of the graph.

    :param graph: Adjacency list representation of the graph
    :return: None
    """
    width = 50
    title = " Undirected Weighted Graph "
    header = title.center(width, '=')
    footer = "=" * width

    print(header)
    for vertex, neighbors in graph.items():
        print(f"\tGraph [{vertex}] → {neighbors}")
    print(footer)
