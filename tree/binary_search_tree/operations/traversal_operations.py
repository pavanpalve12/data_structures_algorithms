from typing import List

from tree.binary_search_tree.helpers import (
    state_helpers as stt_help,
    structural_helpers as str_help
)
from tree.binary_search_tree.schemas.schemas import Tree, Node


# --------------------------------------------------------------------------
# Traversals
# --------------------------------------------------------------------------
def bst_traverse(tree: Tree, traverse_type: str = "preorder") -> List:
    if str_help._is_empty_tree(tree):
        raise ValueError(f"{type} Traverse Failed: bst is empty.")

    metadata = stt_help._compute_metadata(tree)
    result = metadata[traverse_type]
    result = [str(node.data) for node in result]
    return result


# --------------------------------------------------------------------------
# Internal helpers
# --------------------------------------------------------------------------

def _preorder(node: Node) -> List[Node]:
    if node is None:
        return []

    result = [node]
    if node.left:
        result.extend(_preorder(node.left))
    if node.right:
        result.extend(_preorder(node.right))

    return result

def _postorder(node: Node) -> List[Node]:
    if node is None:
        return []

    result = []
    if node.left:
        result.extend(_postorder(node.left))
    if node.right:
        result.extend(_postorder(node.right))
    result.append(node)
    return result

def _inorder(node: Node) -> List[Node]:
    if node is None:
        return []

    result = []
    if node.left:
        result.extend(_inorder(node.left))

    result.append(node)

    if node.right:
        result.extend(_inorder(node.right))

    return result


