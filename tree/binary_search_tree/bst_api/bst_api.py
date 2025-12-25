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
    def __init__(self, data: Any = None):
        if data is None:
            self.tree = Tree()
        else:
            root_node = Node(data)
            self.tree = Tree(root_node)

# --------------------------------------------------------------------------
# Core Operations
# --------------------------------------------------------------------------
    def insert_node(self, value: Any) -> bool:
        new_node = Node(value)
        return core_operations.insert_node(self.tree, new_node)


    def delete_node(self, value: Any) -> bool:
        return core_operations.delete_node(self.tree, value)


    def search_node(self, value: Any) -> Node:
        target_node = core_operations.search_node(self.tree, value)
        if target_node is None:
            raise LookupError(f"Search failed: node with value {value} not found.")
        return target_node
# --------------------------------------------------------------------------
# DFS Traversals
# --------------------------------------------------------------------------
    def dfs_preorder(self):
        return traversal_operations.bst_traverse(self.tree, "preorder")

    def dfs_postorder(self):
        return traversal_operations.bst_traverse(self.tree, "postorder")

    def dfs_inorder(self):
        return traversal_operations.bst_traverse(self.tree, "inorder")

# --------------------------------------------------------------------------
# BFS Traversal
# --------------------------------------------------------------------------
    def bfs_level_order(self):
        return traversal_operations.bst_traverse(self.tree, "bfs")

# --------------------------------------------------------------------------
# State Operations
# --------------------------------------------------------------------------
    def compute_height(self, edges: bool = False) -> int:
        return state_operations.compute_height(self.tree, edges)

    def compute_depth(self, value):
        return state_operations.compute_depth(self.tree, value)

    def compute_size(self):
        return state_operations.compute_size(self.tree)

    def compute_edges(self):
        return state_operations.compute_edges(self.tree)

    def compute_min_node(self):
        return state_operations.compute_min_node(self.tree)

    def compute_max_node(self):
        return state_operations.compute_min_node(self.tree)

# --------------------------------------------------------------------------
# Utilities
# --------------------------------------------------------------------------
    def print_tree(self):
        return visual_operations.print_tree(self.tree)