"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------
This module serves as the **entry point and test harness** for the Undirected
Weighted Graph implementation.

It is intended for:
- Manual testing
- Behavioral verification
- Learning and experimentation

This module:
- Constructs sample weighted graphs
- Invokes core graph operations
- Demonstrates traversals and graph properties
- Exercises weight-aware algorithms
- Prints results for inspection

It is **not intended for production use**.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Create representative weighted test graphs
- Exercise Graph APIs
- Display traversal, cost, and shortest-path outputs
------------------------------------------------------------------------------------
Dependencies
------------------------------------------------------------------------------------
- schemas.Graph
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- Focuses on clarity over automation
- Uses explicit graph construction with weights
- Mirrors real usage patterns of the Graph API
------------------------------------------------------------------------------------
"""

from graph.weighted_undirected_graph.schemas import Graph


def generate_test_graph(graph: Graph) -> None:
    """
    Populate the graph with a predefined weighted structure for testing.

    Structure:

         A
       / | \
     4/  |  \2
     B  1|   C
      \  |  /
      5\ | /3
         D

        E — F

    :param graph: Graph instance to populate
    :return: None
    """
    # Component 1 (cyclic, weighted)
    graph.insert_edge("A", "B", 4)
    graph.insert_edge("A", "C", 2)
    graph.insert_edge("B", "D", 5)
    graph.insert_edge("C", "D", 3)
    graph.insert_edge("A", "D", 1)

    # Component 2 (disconnected)
    graph.insert_edge("E", "F", 7)


def main() -> None:
    """
    Execute weighted graph operations to validate functionality.

    This function:
    - Builds a test graph
    - Prints graph structure
    - Runs BFS and DFS traversals (weight-agnostic)
    - Computes graph properties
    - Tests path-cost computation
    - Runs shortest-path algorithm
    - Performs mutation operations
    - Displays results after each stage

    :return: None
    """
    graph = Graph()
    generate_test_graph(graph)

    print(" Weighted Graph Structure ".center(60, "-"))
    graph.print_graph()
    print("-" * 60)

    print(" Traversals (Weights Ignored) ".center(60, "-"))
    print(f"BFS (Iterative) from A : {graph.bfs_iterative('A')}")
    print(f"BFS (Recursive) from A : {graph.bfs_recursive('A')}")
    print(f"DFS (Iterative) from A : {graph.dfs_iterative('A')}")
    print(f"DFS (Recursive) from A : {graph.dfs_recursive('A')}")
    print("-" * 60)

    print(" Graph Properties ".center(60, "-"))
    print(f"Connected Components : {graph.get_connected_components()}")
    print(f"Cycle Detected       : {graph.detect_cycle('A')}")
    print("-" * 60)

    print(" Path Cost Tests ".center(60, "-"))
    path = ["A", "D", "C"]
    print(f"Path           : {path}")
    print(f"Total Cost     : {graph.get_path_cost(path)}")
    print("-" * 60)

    print(" Shortest Path (Dijkstra) ".center(60, "-"))
    distance, previous = graph.shortest_path_dijkstra("A")
    print(f"Distances from A : {distance}")

    destination = "D"
    shortest_path = graph.shortest_path_to("A", destination)
    print(f"Shortest Path A → {destination} : {shortest_path}")
    print("-" * 60)

    print(" Mutation Tests ".center(60, "-"))
    print("Removing edge A — D")
    graph.remove_edge("A", "D")
    graph.print_graph()

    print("\nRemoving vertex B")
    graph.remove_vertex("B")
    graph.print_graph()
    print("-" * 60)


if __name__ == "__main__":
    main()
