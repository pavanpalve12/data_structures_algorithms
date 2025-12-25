from tree.binary_search_tree.schemas.schemas import Node, Tree

def _is_empty_tree(tree: Tree) -> bool:
    return tree.root is None

def _get_parent(node: Node, target_node: Node):
    if node is None:
        return None

    if node.left == target_node or node.right == target_node:
        return node

    if target_node.data < node.data:
        return _get_parent(node.left, target_node)
    else:
        return _get_parent(node.right, target_node)

def _get_inorder_successor(node: Node):
    if node is None or node.right is None:
        return None

    current = node.right

    while current.left is not None:
        current = current.left
    return current
