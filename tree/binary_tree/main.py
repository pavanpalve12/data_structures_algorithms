"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------
This module serves as the **entry point** for the Normal Binary Tree application.

It is responsible for:
- Initializing the Tree API
- Acting as the execution starting point
- Orchestrating high-level application flow

This module contains no tree implementation logic.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Initialize application components
- Invoke TreeAPI operations for demonstration or usage
- Serve as the program entry point
------------------------------------------------------------------------------------
Public Functions
------------------------------------------------------------------------------------
- main
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- All tree logic is accessed through TreeAPI
- No direct interaction with schemas, helpers, or operations
- No I/O, CLI parsing, or configuration logic is enforced here
------------------------------------------------------------------------------------
"""

from schemas import Node
from tree_api import TreeAPI

def _generate_test_tree():
    """
    Purpose : Generate test tree manually to test dev code
    :return: Tree instance
    """
    tree = TreeAPI("A")

    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    tree.tree.root.left = node_b
    tree.tree.root.right = node_c

    node_b.left = node_d
    node_b.right = node_e

    node_c.left = node_f
    return tree

def main() -> None:
    """
    Purpose: Application entry function
    :return: None
    """
    #tree = _generate_test_tree()
    #tree.print_tree()
    tree = TreeAPI("A")

    tree.insert_node("B")
    tree.insert_node("C")
    tree.insert_node("D")
    tree.insert_node("E")
    tree.insert_node("F")
    tree.insert_node("G")
    tree.insert_node("H")

    tree.print_tree()

    tree.delete_node("G")
    tree.print_tree()

    tree.delete_node("B")
    tree.print_tree()

    print(" Operations ".center(60, '-'))
    target_node = tree.search_node("A")
    print(f"Target Value = {"A"} & Searched Node = {target_node.data} → {target_node}")
    target_node = tree.search_node("F")
    print(f"Target Value = {"F"} & Searched Node = {target_node.data} → {target_node}")
    print("-" * 60)

    print(" Traversal ".center(60, '-'))
    print(f"\tBFS Level Order: {' → '.join(tree.bfs_level_order())}")
    print(f"\tDFS Pre Order: {' → '.join(tree.dfs_preorder())}")
    print(f"\tDFS In Order: {' → '.join(tree.dfs_inorder())}")
    print(f"\tDFS Post Order: {' → '.join(tree.dfs_postorder())}")
    print("-" * 60)

    print(" Metadata ".center(60, '-'))
    print(f"\tSize: {tree.compute_size()}")
    print(f"\tHeight (Level): {tree.compute_height()}")
    print(f"\tHeight (Edges): {tree.compute_height(edges=True)}")
    print(f"\tDepth till {"F"}: {tree.compute_depth("F")}")
    print("-" * 60)

if __name__ == "__main__":
    main()
