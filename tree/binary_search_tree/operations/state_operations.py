from typing import Dict, Any

from tree.binary_search_tree.helpers import (
    structural_helpers as str_help,
    state_helpers as stt_help
)
from tree.binary_search_tree.schemas.schemas import Tree


# --------------------------------------------------------------------------
# State Operations
# --------------------------------------------------------------------------
def compute_height(tree: Tree, edges: bool = False) -> int:
    if str_help._is_empty_tree(tree):
        raise ValueError("Height Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["height_levels"] if not edges else metadata["height_edges"]

def compute_size(tree: Tree) -> int:
    if str_help._is_empty_tree(tree):
        raise ValueError("Size Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["size"]

def compute_depth(tree: Tree, value) -> Dict:
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    depth_map = metadata["depth_map"]

    result = ', '.join(
        [
            res for res in
            {
                f"{node.data} → {level}"
                for node, level in depth_map.items()
                if node.data == value
            }
        ]
    )
    return result

def compute_edges(tree: Tree) -> int:
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["edge_count"]

def compute_min_node(tree: Tree) -> Any:
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["min_node"].data

def compute_max_node(tree: Tree) -> Any:
    if str_help._is_empty_tree(tree):
        raise ValueError("Depth Computation Failed: BST is empty")

    metadata = stt_help._compute_metadata(tree)
    return metadata["max_node"].data


