from typing import Any

from tree.binary_search_tree.schemas.schemas import Node, Tree
from tree.binary_search_tree.operations import (
    core_operations, traversal_operations,
    visual_operations, state_operations
)

# --------------------------------------------------------------------------
# TreeAPI - Public API Class to expose BST operations
# --------------------------------------------------------------------------
class TreeAPI:
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
        return core_operations.insert_ndoe(self.tree, new_node)


    def delete_node(self, value: Any) -> bool:
        return core_operations.delete_node(self.tree, value)


    def search_node(self, value: Any) -> Node:
        return core_operations.search_node(self.tree, value)
# --------------------------------------------------------------------------
# DFS Traversals
# --------------------------------------------------------------------------
    def dfs_preorder(self):
        return traversal_operations.dfs_preorder_traversal(self.tree.root)

    def dfs_postorder(self):
        return traversal_operations.dfs_postorder_traversal(self.tree.root)

    def dfs_inorder(self):
        return traversal_operations.dfs_inorder_traversal(self.tree.root)

# --------------------------------------------------------------------------
# BFS Traversal
# --------------------------------------------------------------------------
    def bfs_level_order(self):
        return traversal_operations.bfs_level_order_traversal([self.tree.root])

# --------------------------------------------------------------------------
# State Operations
# --------------------------------------------------------------------------
    def compute_height(self, edges: bool = False) -> int:
        return state_operations.compute_height(self.tree, edges)

    def compute_depth(self):
        return state_operations.compute_depth(self.tree)

    def compute_size(self):
        return state_operations.compute_size(self.tree)

    def compute_edges(self):
        return state_operations.compute_edges(self.tree)

# --------------------------------------------------------------------------
# Utilities
# --------------------------------------------------------------------------
    def print_tree(self):
        return visual_operations.print_tree(self)