from typing import Dict, List

from tree.binary_search_tree.schemas.schemas import Node, Tree
from tree.binary_search_tree.helpers import (
    structural_helpers as str_help
)

# --------------------------------------------------------------------------
# Compute Metadata -> detailed info on tree
# --------------------------------------------------------------------------
def _compute_metadata(tree: Tree) -> Dict:
    metadata = {
        'nodes': [],
        'bfs': [],
        'preorder': [],
        'inorder': [],
        'postorder': [],
        'parent_map': {},  # child node -> parent or None
        'child_map': {},  # parent node -> [left?, right?]
        'depth_map': {},  # node -> depth (edges)
        'size': 0,
        'edge_count': 0,
        'height_levels': 0,
        'height_edges': -1,
        'min_node': None,
        'max_node': None
    }

    if str_help._is_empty_tree(tree):
        return metadata

    _bfs_metadata([tree.root], 0, metadata)

    metadata["height_edges"] = metadata["height_levels"] - 1
    metadata["inorder"] =  _inorder(tree.root)
    metadata["preorder"] = _preorder(tree.root)
    metadata["postorder"] = _postorder(tree.root)

    return metadata


# --------------------------------------------------------------------------
# Compute Metadata Helper -> BFS for collecting info
# --------------------------------------------------------------------------
def _bfs_metadata(
        level_nodes: List[Node],
        level_index: int,
        metadata: Dict
):

    if not level_nodes:
        return

    metadata["height_levels"] = max(metadata["height_levels"], level_index + 1)

    next_level = []
    for node in level_nodes:
        children = []

        metadata["parent_map"].setdefault(node, None)
        metadata["child_map"].setdefault(node, [])
        metadata["depth_map"].setdefault(node, None)

        metadata["nodes"].append(node)
        metadata["bfs"].append(node)
        metadata["depth_map"][node] = level_index
        metadata["size"] += 1

        if metadata["min_node"] is None or node.data < metadata["min_node"].data:
            metadata["min_node"] = node

        if metadata["max_node"] is None or node.data > metadata["max_node"].data:
            metadata["max_node"] = node

        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

        next_level.extend(children)

        for child in children:
            metadata["edge_count"] += 1
            metadata["parent_map"][child] = node
            metadata["child_map"][node].append(child)

    _bfs_metadata(next_level, level_index + 1, metadata)


# --------------------------------------------------------------------------
# Traversal helpers
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
