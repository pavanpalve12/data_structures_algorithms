"""
------------------------------------------------------------------------------------
Module Name: tree_api
------------------------------------------------------------------------------------
This module defines the **user-facing API layer** for a Normal Binary Tree.

It provides a clean abstraction for interacting with the tree while delegating
all actual operational logic to the underlying `operations` module.

This module is responsible for:
- Exposing a stable public API for tree operations
- Delegating insert, delete, search, and traversal requests
- Acting as the single entry point for tree usage

No tree manipulation logic exists in this module.
------------------------------------------------------------------------------------
Responsibilities
------------------------------------------------------------------------------------
- Expose tree insertion API
- Expose tree deletion API
- Expose tree search API
- Expose DFS and BFS traversal APIs
- Expose tree visualization API
------------------------------------------------------------------------------------
Public Classes
------------------------------------------------------------------------------------
- TreeAPI
------------------------------------------------------------------------------------
Public Methods
------------------------------------------------------------------------------------
- insert_node
- delete_node
- search_node
- dfs_preorder
- dfs_inorder
- dfs_postorder
- bfs_level_order
- print_tree
------------------------------------------------------------------------------------
Design Notes
------------------------------------------------------------------------------------
- TreeAPI contains no operational logic
- All behavior is delegated to the operations module
- This layer must remain thin and stable
- No invariants are enforced at this level
- No I/O or traversal logic is implemented here
------------------------------------------------------------------------------------
"""
from typing import Any

import operations
import structural_helpers
from schemas import Node, Tree


class TreeAPI:
    """
    User-facing API for interacting with a Normal Binary Tree.
    """

    def __init__(self, data: Any) -> None:
        """
        Purpose: Initialize the Tree API
        :return: None
        """
        root_node = Node(data)
        self.tree = Tree(root_node)

    # --------------------------------------------------------------------------
    # Core Operations
    # --------------------------------------------------------------------------
    def insert_node(self, value) -> None:
        """
        Purpose: Insert a value into the binary tree
        :param value: Value to be inserted
        :return: None
        """
        return operations.insert_node(self.tree, value)

    def delete_node(self, value) -> None:
        """
        Purpose: Delete a value from the binary tree
        :param value: Value to be deleted
        :return: None
        """
        return operations.delete_node(self.tree, value)

    def search_node(self, value) -> Node:
        """
        Purpose: Search for a value in the binary tree
        :param value: Value to search for
        :return: Node if value exists, otherwise Error
        """
        return operations.search_node(self.tree, value)

    # --------------------------------------------------------------------------
    # DFS Traversals
    # --------------------------------------------------------------------------
    def dfs_preorder(self):
        """
        Purpose: Traverse the tree using preorder DFS
        :return: Traversal result
        """
        return operations.dfs_preorder(self.tree.root)

    def dfs_inorder(self):
        """
        Purpose: Traverse the tree using inorder DFS
        :return: Traversal result
        """
        return operations.dfs_inorder(self.tree.root)

    def dfs_postorder(self):
        """
        Purpose: Traverse the tree using postorder DFS
        :return: Traversal result
        """
        return operations.dfs_postorder(self.tree.root)

    # --------------------------------------------------------------------------
    # BFS Traversal
    # --------------------------------------------------------------------------
    def bfs_level_order(self):
        """
        Purpose: Traverse the tree using level-order BFS
        :return: Traversal result
        """
        return operations.bfs_level_order([self.tree.root])

    # --------------------------------------------------------------------------
    # Utilities
    # --------------------------------------------------------------------------
    def compute_size(self) -> int:
        """
        Purpose: Return the total number of nodes in the tree
        :return: Total number of nodes
        """
        return structural_helpers.compute_size(self.tree)

    def compute_height(self, edges: bool = False) -> int:
        """
        Purpose: Return the height of the tree
        :param edges: If True, compute height in edges; otherwise in levels
        :return: Height of the tree
        """
        return structural_helpers.compute_height(self.tree, edges)

    def compute_depth(self, value) -> int:
        """
        Purpose: Return the depth of a given node from the root
        :param value: Value to search for
        :return: Depth of the node
        """
        return structural_helpers.compute_depth(self.tree, value)

    def print_tree(self) -> None:
        """
        Purpose: Print the tree structure
        :return: None
        """
        return operations.print_tree(self.tree)
