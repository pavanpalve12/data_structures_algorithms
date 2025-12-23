"""
------------------------------------------------------------------------------------
Module: tree_api
------------------------------------------------------------------------------------

Public API for interacting with a generic linked tree.

This module acts as a **facade** over internal schema, operations,
and helper modules. External consumers interact exclusively through
TreeAPI.

Design goals:
- Value-based public interface
- Hide Node and internal implementation details
- Centralize access to all tree operations
- Allow internal refactors without API breakage
------------------------------------------------------------------------------------
"""

from typing import Any, Optional
from schemas import Tree, Node
import operations
import helpers


class TreeAPI:
    """
    Public interface for a generic linked tree.

    TreeAPI manages a Tree instance and exposes a safe, high-level,
    value-based API for tree manipulation and inspection.
    """

    def __init__(self, data: Optional[Any] = None):
        """
        Initialize the tree with an optional root value.

        :param data: Value for the root node, or None to create an empty tree
        """
        root_node = Node(data) if data is not None else None
        self.tree = Tree(root_node)

    def insert_node(self, child_data: Any, parent_data: Any) -> None:
        """
        Insert a new node under the specified parent.

        :param child_data: Value for the new child node
        :param parent_data: Value identifying the parent node
        """
        operations.insert_node(self.tree, child_data, parent_data)

    def delete_node(self, target_data: Any) -> None:
        """
        Delete a node and its entire subtree.

        :param target_data: Value identifying the node to delete
        """
        operations.delete_node(self.tree, target_data)

    def search_node(self, target_data: Any) -> Optional[Node]:
        """
        Search for a node by value.

        :param target_data: Value identifying the node
        :return: Matching Node if found, else None
        """
        return operations.search_node(self.tree, target_data)

    def dfs_preorder(self) -> list[Any]:
        """
        Perform preorder depth-first traversal.

        :return: List of node values in preorder
        """
        return operations.dfs_preorder(self.tree.root)

    def dfs_postorder(self) -> list[Any]:
        """
        Perform postorder depth-first traversal.

        :return: List of node values in postorder
        """
        return operations.dfs_postorder(self.tree.root)

    def bfs_traversal(self) -> list[Any]:
        """
        Perform breadth-first (level-order) traversal.

        :return: List of node values in BFS order
        """
        return [] if self.tree.root is None else operations.bfs_traversal([self.tree.root])

    def compute_height(self, edges: bool = False) -> int:
        """
        Compute the height of the tree.

        :param edges: If True, measure height in edges; otherwise in levels
        :return: Height of the tree
        """
        return helpers.compute_height(self.tree, edges)

    def compute_depth(self, target_data: Any) -> int:
        """
        Compute the depth of a node identified by value.

        :param target_data: Value identifying the node
        :return: Depth of the node
        """
        return helpers.compute_depth(self.tree, target_data)

    def compute_size(self) -> int:
        """
        Compute the total number of nodes in the tree.

        :return: Node count
        """
        return helpers.compute_size(self.tree)

    def print_tree(self) -> None:
        """
        Print the tree in a human-readable level-order format.

        Intended for visualization and debugging only.
        """
        helpers.bfs_print(self.tree)
