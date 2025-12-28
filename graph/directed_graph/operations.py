"""
------------------------------------------------------------------------------------
Module Name: operations
------------------------------------------------------------------------------------
This module implements the **behavior and algorithms** for the Directed Graph
data structure.

It contains mutation logic, traversal algorithms, and graph property computations
that operate on the adjacency list stored in `Graph.graph`.

------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Implement vertex and edge insert/remove operations
- Implement BFS and DFS (iterative and recursive)
- Implement cycle detection for directed graphs
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
- detect_cycle
- print_graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Functions operate on adjacency-list dictionary (`Graph.graph`)
- Edges are directional (u → v)
- Traversal follows outgoing edges only
- No I/O or persistence logic exists in this module
------------------------------------------------------------------------------------
"""
from collections import deque
from typing import Any, List, Set
from schemas import Graph


# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
def insert_vertex(graph: Graph, vertex: Any) -> None:
    """
    Add a vertex to the directed graph.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Vertex identifier
    :return: None
    """
    if _vertex_exists(graph, vertex):
        return

    graph[vertex] = []


def insert_edge(graph: Graph, from_vertex: Any, to_vertex: Any) -> None:
    """
    Add a directed edge (from_vertex → to_vertex).

    :param graph: Adjacency list (Graph.graph)
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: None
    """
    if not _vertex_exists(graph, from_vertex):
        graph[from_vertex] = []
    if not _vertex_exists(graph, to_vertex):
        graph[to_vertex] = []

    if _edge_exists(graph, from_vertex, to_vertex):
       return

    graph[from_vertex].append(to_vertex)


def remove_vertex(graph: Graph, vertex: Any) -> None:
    """
    Remove a vertex and all incoming and outgoing edges.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Vertex to remove
    :return: None
    """
    if not _vertex_exists(graph, vertex):
        return

    # outgoing edges
    graph[vertex].clear()

    # incoming edges
    for vtx in graph:
        if vertex in graph[vtx]:
            remove_edge(graph, vtx, vertex)

    del graph[vertex]

def remove_edge(graph: Graph, from_vertex: Any, to_vertex: Any) -> None:
    """
    Remove a directed edge (from_vertex → to_vertex).

    :param graph: Adjacency list (Graph.graph)
    :param from_vertex: Source vertex
    :param to_vertex: Destination vertex
    :return: None
    """
    if not _edge_exists(graph, from_vertex, to_vertex):
        return

    graph[from_vertex].remove(to_vertex)


# ----------------------------------------------------------------------
# Traversals
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
    if not vertex:
        return visited

    visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited

# ----------------------------------------------------------------------
# Graph Properties
# ----------------------------------------------------------------------
def detect_cycle(graph: Graph) -> bool:
    """
    Detect whether a directed graph contains a cycle.

    Uses Depth-First Search (DFS) with recursion-stack tracking.
    A cycle is detected if a vertex is encountered that is already
    present in the current recursion stack.

    :param graph: Adjacency list (Graph.graph)
    :return: True if a cycle exists, otherwise False
    """
    visited = set()
    rec_stack = set()

    for vertex in graph:
        if vertex not in visited:
            if _detect_cycle_dfs(graph, vertex, visited, rec_stack):
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
    title = " Directed Graph  "
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

def _detect_cycle_dfs(
        graph: Graph,
        vertex: Any,
        visited: Set[Any],
        rec_stack: Set[Any]
) -> bool:
    """
    Recursive helper for directed cycle detection.

    Performs DFS from the given vertex while tracking the current
    recursion path using a recursion stack.

    :param graph: Adjacency list (Graph.graph)
    :param vertex: Current vertex in DFS
    :param visited: Set of fully visited vertices
    :param rec_stack: Set of vertices in the current DFS path
    :return: True if a cycle is detected, otherwise False
    """
    if vertex is None:
        return False

    visited.add(vertex)
    rec_stack.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if _detect_cycle_dfs(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(vertex)
    return False
