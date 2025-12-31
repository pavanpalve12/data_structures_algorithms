"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements the **behavior and algorithms** for the Directed Weighted
Graph data structure.

It reuses traversal and structural logic from the unweighted graph implementation
and extends it with weight-aware operations such as shortest path computation.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement vertex and edge insert/remove operations
- Implement BFS and DFS (iterative and recursive)
- Implement weight-aware algorithms (path cost, shortest paths)

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All functions operate on adjacency-list dictionary (`Graph.graph`)
- Adjacency list format: vertex -> List[(neighbor, weight)]
- Traversals follow **edge direction**
- Graph schema is treated as a data container only
------------------------------------------------------------------------------------
"""

import heapq
from collections import deque
from typing import Any, List, Dict, Tuple, Optional


# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
def insert_vertex(graph: Dict[Any, List[Tuple[Any, Any]]], vertex: Any) -> None:
    """
    Add a vertex to the graph if it does not already exist.

    :param graph: Adjacency list representation of the graph
    :param vertex: Vertex identifier
    :return: None
    """
    if vertex not in graph:
        graph[vertex] = []


def insert_edge(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any,
        weight: Any
) -> None:
    """
    Add or update a directed weighted edge (u → v).

    :param graph: Adjacency list representation of the graph
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :param weight: Weight associated with the edge
    :return: None
    """
    if from_vertex not in graph:
        graph[from_vertex] = []

    if to_vertex not in graph:
        graph[to_vertex] = []

    for vtx, wgt in graph[from_vertex]:
        if vtx == to_vertex:
            if wgt == weight:
                return
            graph[from_vertex].remove((vtx, wgt))
            graph[from_vertex].append((to_vertex, weight))
            return

    graph[from_vertex].append((to_vertex, weight))


def update_edge_weight(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any,
        weight: Any
) -> None:
    """
    Update the weight of an existing directed edge.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :param weight: New weight
    :return: None
    """
    if from_vertex not in graph or to_vertex not in graph:
        return

    for vtx, wgt in graph[from_vertex]:
        if vtx == to_vertex:
            if wgt == weight:
                return
            graph[from_vertex].remove((vtx, wgt))
            graph[from_vertex].append((to_vertex, weight))
            return

    graph[from_vertex].append((to_vertex, weight))


def get_edge_weight(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any
) -> Optional[Any]:
    """
    Retrieve the weight associated with a directed edge.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: Edge weight if present, otherwise None
    """
    if from_vertex not in graph:
        return None

    for vtx, wgt in graph[from_vertex]:
        if vtx == to_vertex:
            return wgt

    return None


def remove_vertex(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        vertex: Any
) -> None:
    """
    Remove a vertex and all its incident edges (incoming and outgoing).

    :param graph: Adjacency list representation
    :param vertex: Vertex to remove
    :return: None
    """
    if vertex not in graph:
        return

    # Remove outgoing edges
    del graph[vertex]

    # Remove incoming edges
    for vtx in graph:
        graph[vtx] = [
            (n, w) for n, w in graph[vtx] if n != vertex
        ]


def remove_edge(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any
) -> None:
    """
    Remove a directed edge (u → v).

    :param graph: Adjacency list representation
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: None
    """
    if from_vertex in graph:
        graph[from_vertex] = [
            (n, w) for n, w in graph[from_vertex] if n != to_vertex
        ]


# ----------------------------------------------------------------------
# BFS Traversal (direction-aware, weight-agnostic)
# ----------------------------------------------------------------------
def bfs_iterative(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        start_vertex: Any
) -> List[Any]:
    """
    Perform iterative Breadth-First Search (BFS) following edge direction.

    :param graph: Adjacency list representation
    :param start_vertex: Starting vertex
    :return: BFS traversal order
    """
    visited = []
    queue = deque([start_vertex])

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)

            for neighbor, _ in graph.get(current, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited


def bfs_recursive(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        level_vertices: List[Any],
        visited: List[Any]
) -> List[Any]:
    """
    Perform recursive BFS (level-based) following edge direction.

    :param graph: Adjacency list representation
    :param level_vertices: Current BFS frontier
    :param visited: Visited vertices
    :return: BFS traversal order
    """
    if not level_vertices:
        return visited

    next_level = []

    for vertex in level_vertices:
        if vertex not in visited:
            visited.append(vertex)

        for neighbor, _ in graph.get(vertex, []):
            if neighbor not in visited:
                next_level.append(neighbor)

    return bfs_recursive(graph, next_level, visited)


# ----------------------------------------------------------------------
# DFS Traversals (direction-aware, weight-agnostic)
# ----------------------------------------------------------------------
def dfs_iterative(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        start_vertex: Any
) -> List[Any]:
    """
    Perform iterative Depth-First Search (DFS) following edge direction.

    :param graph: Adjacency list representation
    :param start_vertex: Starting vertex
    :return: DFS traversal order
    """
    visited = []
    stack = [start_vertex]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

            for neighbor, _ in graph.get(current, []):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


def dfs_recursive(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        vertex: Any,
        visited: List[Any]
) -> List[Any]:
    """
    Perform recursive Depth-First Search (DFS) following edge direction.

    :param graph: Adjacency list representation
    :param vertex: Current vertex
    :param visited: Visited vertices
    :return: DFS traversal order
    """
    if vertex is None or vertex in visited:
        return visited

    visited.append(vertex)

    for neighbor, _ in graph.get(vertex, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


# ----------------------------------------------------------------------
# Weight-Aware Algorithms
# ----------------------------------------------------------------------
def get_path_cost(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        path: List[Any]
) -> Optional[Any]:
    """
    Compute total cost of a given directed path.

    :param graph: Adjacency list representation
    :param path: List of vertices
    :return: Total cost or None if invalid path
    """
    total_cost = 0

    for index in range(len(path) - 1):
        from_vertex = path[index]
        to_vertex = path[index + 1]

        weight = get_edge_weight(graph, from_vertex, to_vertex)
        if weight is None:
            return None

        total_cost += weight

    return total_cost


def shortest_path_dijkstra(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        source: Any
) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
    """
    Compute shortest paths from source using Dijkstra's algorithm.

    :param graph: Adjacency list representation
    :param source: Source vertex
    :return: Distance map and predecessor map
    """
    distance = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}

    distance[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distance[current_vertex]:
            continue

        for neighbor, weight in graph.get(current_vertex, []):
            alt_distance = distance[current_vertex] + weight

            if alt_distance < distance[neighbor]:
                distance[neighbor] = alt_distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (alt_distance, neighbor))

    return distance, previous


def shortest_path_to(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        source: Any,
        destination: Any
) -> List[Any]:
    """
    Reconstruct shortest directed path between two vertices.

    :param graph: Adjacency list representation
    :param source: Source vertex
    :param destination: Destination vertex
    :return: Shortest path as list of vertices
    """
    _, previous = shortest_path_dijkstra(graph, source)
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path if path and path[0] == source else []


# ----------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------
def print_graph(graph: Dict[Any, List[Tuple[Any, Any]]]) -> None:
    """
    Print adjacency list of directed weighted graph.

    :param graph: Adjacency list representation
    :return: None
    """
    width = 50
    title = " Directed Weighted Graph "
    print(title.center(width, "="))
    for vertex, neighbors in graph.items():
        print(f"\tGraph [{vertex}] → {neighbors}")
    print("=" * width)
