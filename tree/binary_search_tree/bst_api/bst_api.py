"""
------------------------------------------------------------------------------------
Module Name: bst_api
------------------------------------------------------------------------------------
This module defines the **public-facing API** for interacting with a Binary
Search Tree (BST).

It exposes a clean, minimal interface for consumers while delegating all
implementation details to internal operation, traversal, state, and helper
modules.

This module is responsible for:
- Tree initialization
- Exposing core BST operations (insert, delete, search)
- Exposing traversal interfaces (DFS, BFS)
- Exposing tree state computations
- Providing utility functions for visualization

No business logic or invariants are implemented here directly.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Act as a facade over BST internal modules
- Provide a stable, user-friendly interface
- Hide internal tree representation and mechanics
------------------------------------------------------------------------------------
Public Classes
------------------------------------------------------------------------------------
- BSTApi
------------------------------------------------------------------------------------
Internal / Helper Classes
------------------------------------------------------------------------------------
None
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- This module delegates all logic to underlying modules
- It does not perform invariant checks directly
- It does not manipulate tree internals directly
- Acts as the single entry point for BST consumers
------------------------------------------------------------------------------------
"""

from typing import Any

from tree.binary_search_tree.operations import (
    core_operations, traversal_operations,
    visual_operations, state_operations
)
from tree.binary_search_tree.schemas.schemas import Node, Tree


# --------------------------------------------------------------------------
# TreeAPI - Public API Class to expose BST operations
# --------------------------------------------------------------------------
class BSTApi:
    """
    Public API facade for interacting with a Binary Search Tree.

    This class provides a high-level interface for tree operations while
    delegating all underlying logic to internal modules.
    """

    def __init__(self, data: Any = None):
        """
        Initialize the BST API.

        :param data: Optional value to initialize the root node of the tree.
        """
        if data is None:
            self.tree = Tree()
        else:
            root_node = Node(data)
            self.tree = Tree(root_node)

    # ----------------------------------------------------------------------
    # Core Operations
    # ----------------------------------------------------------------------
    def insert_node(self, value: Any) -> bool:
        """
        Insert a value into the Binary Search Tree.

        :param value: Value to be inserted into the tree.
        :return: True if insertion succeeds.
        """
        new_node = Node(value)
        return core_operations.insert_node(self.tree, new_node)

    def delete_node(self, value: Any) -> bool:
        """
        Delete a value from the Binary Search Tree.

        :param value: Value to be deleted from the tree.
        :return: True if deletion succeeds, False otherwise.
        """
        return core_operations.delete_node(self.tree, value)

    def search_node(self, value: Any) -> Node:
        """
        Search for a value in the Binary Search Tree.

        :param value: Value to search for.
        :return: Node containing the value.
        :raises LookupError: If the value is not found in the tree.
        """
        target_node = core_operations.search_node(self.tree, value)
        if target_node is None:
            raise LookupError(f"Search failed: node with value {value} not found.")
        return target_node

    # ----------------------------------------------------------------------
    # DFS Traversals
    # ----------------------------------------------------------------------
    def dfs_preorder(self):
        """
        Perform a preorder depth-first traversal of the tree.

        :return: List of nodes visited in preorder sequence.
        """
        return traversal_operations.bst_traverse(self.tree, "preorder")

    def dfs_postorder(self):
        """
        Perform a postorder depth-first traversal of the tree.

        :return: List of nodes visited in postorder sequence.
        """
        return traversal_operations.bst_traverse(self.tree, "postorder")

    def dfs_inorder(self):
        """
        Perform an inorder depth-first traversal of the tree.

        :return: List of nodes visited in inorder sequence.
        """
        return traversal_operations.bst_traverse(self.tree, "inorder")

    # ----------------------------------------------------------------------
    # BFS Traversal
    # ----------------------------------------------------------------------
    def bfs_level_order(self):
        """
        Perform a level-order (BFS) traversal of the tree.

        :return: List of nodes visited in level-order sequence.
        """
        return traversal_operations.bst_traverse(self.tree, "bfs")

    # ----------------------------------------------------------------------
    # State Operations
    # ----------------------------------------------------------------------
    def compute_height(self, edges: bool = False) -> int:
        """
        Compute the height of the tree.

        :param edges: If True, height is returned in terms of edges.
                      Otherwise, height is returned in terms of levels.
        :return: Height of the tree.
        """
        return state_operations.compute_height(self.tree, edges)

    def compute_depth(self, value):
        """
        Compute the depth of a given node in the tree.

        :param value: Value of the node whose depth is to be computed.
        :return: Depth of the node.
        """
        return state_operations.compute_depth(self.tree, value)

    def compute_size(self):
        """
        Compute the total number of nodes in the tree.

        :return: Number of nodes in the tree.
        """
        return state_operations.compute_size(self.tree)

    def compute_edges(self):
        """
        Compute the total number of edges in the tree.

        :return: Number of edges in the tree.
        """
        return state_operations.compute_edges(self.tree)

    def compute_min_node(self):
        """
        Retrieve the minimum-valued node in the tree.

        :return: Node with the minimum value.
        """
        return state_operations.compute_min_node(self.tree)

    def compute_max_node(self):
        """
        Retrieve the maximum-valued node in the tree.

        :return: Node with the maximum value.
        """
        return state_operations.compute_min_node(self.tree)

    # ----------------------------------------------------------------------
    # Utilities
    # ----------------------------------------------------------------------
    def print_tree(self):
        """
        Print a visual representation of the tree structure.

        :return: Formatted tree representation.
        """
        return visual_operations.print_tree(self.tree)
