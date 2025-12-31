"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements the **behavior and algorithms** for the Undirected Weighted
Graph data structure.

It reuses traversal and structural logic from the unweighted graph implementation
and extends it with weight-aware operations such as shortest path computation.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement vertex and edge insert/remove operations
- Implement BFS and DFS (iterative and recursive)
- Implement connected components logic
- Implement cycle detection for undirected graphs
- Implement weight-aware algorithms (path cost, shortest paths)

------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All functions operate on adjacency-list dictionary (`Graph.graph`)
- Adjacency list format: vertex -> List[(neighbor, weight)]
- Traversals ignore weights
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
    :type graph: Dict[Any, List[Tuple[Any, Any]]]
    :param vertex: Vertex identifier
    :type vertex: Any
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
    Add or update an undirected weighted edge between two vertices.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
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
            graph[to_vertex].remove((from_vertex, wgt))
            graph[from_vertex].append((to_vertex, weight))
            graph[to_vertex].append((from_vertex, weight))
            return

    graph[from_vertex].append((to_vertex, weight))
    graph[to_vertex].append((from_vertex, weight))


def update_edge_weight(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any,
        weight: Any
) -> None:
    """
    Update the weight of an existing undirected edge.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
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
            graph[to_vertex].remove((from_vertex, wgt))
            graph[from_vertex].append((to_vertex, weight))
            graph[to_vertex].append((from_vertex, weight))
            return

    graph[from_vertex].append((to_vertex, weight))
    graph[to_vertex].append((from_vertex, weight))


def get_edge_weight(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any
) -> Optional[Any]:
    """
    Retrieve the weight associated with an undirected edge.

    :param graph: Adjacency list representation of the graph
    :param from_vertex: One endpoint of the edge
    :param to_vertex: Other endpoint of the edge
    :return: Edge weight if present, otherwise None
    """
    if from_vertex not in graph or to_vertex not in graph:
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
    Remove a vertex and all its incident edges.

    :param graph: Adjacency list representation
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


def remove_edge(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        from_vertex: Any,
        to_vertex: Any
) -> None:
    """
    Remove an undirected edge.

    :param graph: Adjacency list representation
    :param from_vertex: One endpoint
    :param to_vertex: Other endpoint
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
def bfs_iterative(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        start_vertex: Any
) -> List[Any]:
    """
    Perform iterative Breadth-First Search (BFS).

    :param graph: Adjacency list representation
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


def bfs_recursive(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        level_vertices: List[Any],
        visited: List[Any]
) -> List[Any]:
    """
    Perform recursive BFS (level-based).

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

        for neighbor, _ in graph[vertex]:
            if neighbor not in visited:
                next_level.append(neighbor)

    return bfs_recursive(graph, next_level, visited)


# ----------------------------------------------------------------------
# DFS Traversals (weight-agnostic)
# ----------------------------------------------------------------------
def dfs_iterative(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        start_vertex: Any
) -> List[Any]:
    """
    Perform iterative Depth-First Search (DFS).

    :param graph: Adjacency list representation
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


def dfs_recursive(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        vertex: Any,
        visited: List[Any]
) -> List[Any]:
    """
    Perform recursive Depth-First Search (DFS).

    :param graph: Adjacency list representation
    :param vertex: Current vertex
    :param visited: Visited vertices
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
# Graph Properties
# ----------------------------------------------------------------------
def get_connected_components(
        graph: Dict[Any, List[Tuple[Any, Any]]]
) -> int:
    """
    Compute number of connected components.

    :param graph: Adjacency list representation
    :return: Count of connected components
    """
    covered = list(graph.keys())
    connected_count = 0

    while covered:
        visited = bfs_recursive(graph, [covered[0]], [])
        for vertex in visited:
            covered.remove(vertex)
        connected_count += 1

    return connected_count


def detect_cycle(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        start_vertex: Any
) -> bool:
    """
    Detect cycle in undirected graph using DFS with parent tracking.

    :param graph: Adjacency list representation
    :param start_vertex: Starting vertex
    :return: True if cycle exists
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
def get_path_cost(
        graph: Dict[Any, List[Tuple[Any, Any]]],
        path: List[Any]
) -> Optional[Any]:
    """
    Compute total cost of a given path.

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

        for neighbor, weight in graph[current_vertex]:
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
    Reconstruct shortest path between two vertices.

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
    Print adjacency list of weighted graph.

    :param graph: Adjacency list representation
    :return: None
    """
    width = 50
    title = " Undirected Weighted Graph "
    print(title.center(width, "="))
    for vertex, neighbors in graph.items():
        print(f"\tGraph [{vertex}] → {neighbors}")
    print("=" * width)
