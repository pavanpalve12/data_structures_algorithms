from tree.binary_search_tree.bst_api.bst_api import BSTApi
from tree.binary_search_tree.schemas.schemas import Node, Tree

def generate_test_tree(tree):
    n10 = Node(10)
    n8 = Node(8)
    n12 = Node(12)
    n11 = Node(11)
    n13 = Node(13)

    n20 = Node(20)
    n18 = Node(18)
    n25 = Node(25)
    n22 = Node(22)
    n27 = Node(27)

    n10.left = n8
    n10.right = n12

    n8.left = None
    n8.right = None

    n12.left = n11
    n12.right = n13

    n11.left = None
    n11.right = None

    n13.left = None
    n13.right = None

    n20.left = n18
    n20.right = n25

    n18.left = None
    n18.right = None

    n25.left = n22
    n25.right = n27

    n22.left = None
    n22.right = None

    n27.left = None
    n27.right = None

    tree.tree.root.left = n10
    tree.tree.root.right = n20


def main():
    tree = BSTApi(15)
    generate_test_tree(tree)

    tree.insert_node(100)

    tree.print_tree()

    tree.delete_node(100)
    tree.delete_node(15)
    tree.print_tree()



    print(" Operations ".center(60, '-'))
    print("-" * 60)

    print(" Metadata ".center(60, '-'))
    print(f"\tSize: {tree.compute_size()}")
    print(f"\tHeight (Level): {tree.compute_height()}")
    print(f"\tHeight (Edges): {tree.compute_height(edges=True)}")
    print(f"\tDepth for {22}: {tree.compute_depth(22)}")
    print(f"\tMin Node: {tree.compute_min_node()}")
    print(f"\tMax node: {tree.compute_max_node()}")
    print("-" * 60)

    print(" Traversal ".center(60, '-'))
    print(f"BFS Level Order: {' → '.join(tree.bfs_level_order())}")
    print(f"DFS Pre Order: {' → '.join(tree.dfs_preorder())}")
    print(f"DFS In Order: {' → '.join(tree.dfs_inorder())}")
    print(f"DFS Post Order: {' → '.join(tree.dfs_postorder())}")
    print("-" * 60)

if __name__ == '__main__':
    main()