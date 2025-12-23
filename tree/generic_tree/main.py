"""
------------------------------------------------------------------------------------
Module Name: main
------------------------------------------------------------------------------------

This module serves as the **consumer / test harness** for the tree library.

It imports the public TreeAPI only and must not depend on internal modules.

------------------------------------------------------------------------------------
Design Principles
------------------------------------------------------------------------------------
- No internal imports
- No knowledge of implementation details
- Used for testing and experimentation

------------------------------------------------------------------------------------
"""

from tree_api import TreeAPI
from schemas import Node

def main() -> None:
    """
    Purpose: Entry point for tree API testing
    :return: None
    """
    tree = TreeAPI("A")
    tree.insert_node("B", "A")
    tree.insert_node("C", "A")
    tree.insert_node("D", "A")

    tree.insert_node("E", "B")
    tree.insert_node("F", "B")

    tree.insert_node("G", "E")
    tree.insert_node("H", "E")

    tree.insert_node("I", "F")

    tree.insert_node("J", "D")
    tree.insert_node("K", "D")
    tree.insert_node("L", "D")

    tree.insert_node("M", "J")
    tree.insert_node("N", "J")

    target_node = tree.search_node("C")
    print(target_node, target_node.data)
    tree.print_tree()

    tree.delete_node("C")
    tree.print_tree()

    print("\n--------------------------- Traversals ---------------------------------")
    print(f"DFS Preorder: {' → '.join(tree.dfs_preorder())}")
    print(f"DFS Postorder: {' → '.join(tree.dfs_postorder())}")
    print(f"BFS Traversal: {' → '.join(tree.bfs_traversal())}")
    print("-----------------------------------------------------------------------")
    print("\n------------------------------ Stats -----------------------------------")
    print(f"\tHeight (Levels) → {tree.compute_height()}")
    print(f"\tHeight (Edges) → {tree.compute_height(edges=True)}")
    print(f"\tDepth at 'K' → {tree.compute_depth("K")}")
    print(f"\tSize → {tree.compute_size()}")
    print("-----------------------------------------------------------------------")

    """
    tree = TreeAPI("A")
    n1 = Node("B")
    n2 = Node("C")
    n3 = Node("D")
    n4 = Node("E")
    n5 = Node("F")

    tree.tree.root.children = [n1, n2]
    n1.children = [n3, n4]
    n3.children = [n5]

    n1.parent = n2.parent = tree.tree.root
    n3.parent = n4.parent = n1
    n5.parent = n3
    
    # ------------------- Traversal using Recursion -----------------------
    # -------- Preorder --------------------------------------
    def dfs_preorder(node):
        if node is None:
            return []
        result = [node.data]
        for child in node.children:
            result.extend(dfs_preorder(child))
        return result

    node = tree.tree.root
    result = dfs_preorder(node)
    print(
        f"---------- Recursive DFS Preorder ----------\n"
        f"\t{"->".join(result)}\n"
        f"{"-" * len('---------- Recursive DFS Preorder ----------')}"
    )

    # -------- Postorder --------------------------------------
    def dfs_postorder(node):
        if node is None:
            return
        result = []
        for child in node.children:
            result.extend(dfs_postorder(child))

        result.append(node.data)
        return result

    node = tree.tree.root
    result = dfs_postorder(node)
    print(
        f"---------- Recursive DFS Postorder ----------\n"
        f"\t{"->".join(result)}\n"
        f"{"-" * len('---------- Recursive DFS Postorder 1 ----------')}"
    )

    # -------- BFS --------------------------------------
    def bfs(level_nodes):
        if not level_nodes:
            return []

        result = []
        next_level = []

        for node in level_nodes:
            result.append(node.data)

            for child in node.children:
                next_level.append(child)
        result.extend(bfs(next_level))
        return result
    node = tree.tree.root
    result = bfs([node])
    print(
        f"------------- BFS --------------\n"
        f"\t{"->".join(result)}\n"
        f"{"-" * len('------------- BFS --------------')}"
    )

    # ------------------- BFS Search Node -----------------------
    def bfs_search_node(level_nodes, target_node_data):
        if not level_nodes:
            return None

        next_level = []
        for node in level_nodes:
            if node.data == target_node_data:
                return node

            for child in node.children:
                next_level.append(child)
        return bfs_search_node(next_level, target_node_data)

    result = bfs_search_node([tree.tree.root], "C")
    print(f"{result} & {result.data}")

    # ------------------- DFS Search Node -----------------------
    # if node is None:
    #     return []
    # result = [node.data]
    # for child in node.children:
    #     result.extend(dfs_preorder(child))
    # return result

    def dfs_search_node(node, target_node_data):
        if node is None:
            return None

        print(f"Current Node = {node.data}")

        if node.data == target_node_data:
            print(f"Node Found = {node.data}")
            return node

        for child in node.children:
            print(f"Current Child Node = {child.data}")
            found_node = dfs_search_node(child, target_node_data)

            if found_node is not None:
                return found_node
        return None

    node = tree.tree.root
    result = dfs_search_node(node, "X")
    if result is not None:
        print(f"{result} & {result.data}")
    else:
        print("Node not found")

    # ------------------- BFS Print Tree -----------------------
    def bfs_print(level_nodes, level):
        if not level_nodes:
            return ""

        next_level = []
        print(f"Level {level} -> {", ".join(n.data for n in level_nodes)}")
        for node in level_nodes:
            for child in node.children:
                next_level.append(child)
        level += 1
        bfs_print(next_level, level)
        return ""

    bfs_print([tree.tree.root], 0)

    # ------------------- DFS Print Tree -----------------------
    def dfs_print(node, prefix="", is_last=True, is_root=True):
        if node is None:
            return

        if is_root:
            print(node.data)
        else:
            connector = "└─ " if is_last else "├─ "
            print(prefix + connector + node.data)

        # Update prefix for children
        if is_root:
            new_prefix = ""
        else:
            new_prefix = prefix + ("   " if is_last else "│  ")

        child_count = len(node.children)
        for idx, child in enumerate(node.children):
            dfs_print(
                child,
                prefix=new_prefix,
                is_last=(idx == child_count - 1),
                is_root=False
            )

    dfs_print(tree.tree.root)
    """

if __name__ == "__main__":
    main()
