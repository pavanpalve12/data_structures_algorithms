"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------
This module serves as the **entry point and test harness** for the Directed Graph
implementation.

It is intended for:
- Manual testing
- Behavioral verification
- Learning and experimentation

This module:
- Constructs sample directed graphs
- Invokes core graph operations
- Demonstrates traversals and cycle detection
- Prints results for inspection

It is **not intended for production use**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Create representative directed test graphs
- Exercise Graph APIs
- Display traversal and property outputs
------------------------------------------------------------------------------------
Dependencies
------------------------------------------------------------------------------------
- schemas.Graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Focuses on clarity over automation
- Uses explicit graph construction
- Mirrors real usage patterns of the Graph API
------------------------------------------------------------------------------------
"""

from graph.directed_graph.schemas import Graph


def generate_test_graph(graph: Graph) -> None:
    """
    Populate the graph with a predefined directed structure for testing.

    The generated graph contains:
    - One directed cycle
    - One acyclic path

    Structure:

        A → B → C → D
            ↑       ↓
            F ← E ←-

        G → H

    :param graph: Graph instance to populate
    :return: None
    """
    # Directed cycle
    graph.insert_edge("A", "B")
    graph.insert_edge("B", "C")
    graph.insert_edge("C", "D")
    graph.insert_edge("D", "E")
    graph.insert_edge("E", "F")
    graph.insert_edge("F", "B")

    # Separate acyclic component
    graph.insert_edge("G", "H")


def main() -> None:
    """
    Execute directed graph operations to validate functionality.

    This function:
    - Builds a test graph
    - Prints graph structure
    - Runs BFS and DFS traversals
    - Detects cycles
    - Performs mutation operations
    - Displays results after each stage

    :return: None
    """
    graph = Graph()
    generate_test_graph(graph)

    print(" Directed Graph Structure ".center(60, "-"))
    graph.print_graph()
    print("-" * 60)

    print(" Traversals ".center(60, "-"))
    print(f"BFS (Iterative) from A : {graph.bfs_iterative('A')}")
    print(f"BFS (Recursive) from A : {graph.bfs_recursive('A')}")
    print(f"DFS (Iterative) from A : {graph.dfs_iterative('A')}")
    print(f"DFS (Recursive) from A : {graph.dfs_recursive('A')}")
    print("-" * 60)

    print(" Graph Properties ".center(60, "-"))
    print(f"Cycle Detected : {graph.detect_cycle()}")
    print("-" * 60)

    print(" Mutation Tests ".center(60, "-"))
    print("Removing edge B → C")
    graph.remove_edge("B", "C")
    graph.print_graph()

    print("\nRemoving vertex D")
    graph.remove_vertex("D")
    graph.print_graph()
    print("-" * 60)


if __name__ == "__main__":
    main()
