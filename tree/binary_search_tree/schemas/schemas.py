from typing import Any

# --------------------------------------------------------------------------
# Node - represents node in BST
# --------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# --------------------------------------------------------------------------
# Tree - represents BST tree
# --------------------------------------------------------------------------
class Tree:
    def __init__(self, root: Any = None):
        self.root = root if root is not None else None
