"""
------------------------------------------------------------------------------------
Module Name: update_operations
------------------------------------------------------------------------------------

This module defines update and modification operations for a doubly linked
list structure.

Available functions:
- update_node_value
- update_value_at_position
- replace_all_occurrences
- swap_nodes
- relink_nodes

All functions are placeholders and expect the doubly linked list (dll) to be
passed explicitly as the first argument.
------------------------------------------------------------------------------------
"""

def update_node_value(dll, node, new_value):
    """
    Update the value stored in a given node.

    :param dll: Doubly linked list object
    :param node: Node whose value will be updated
    :param new_value: New value to assign to the node
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Update Failed: linked list is empty.")

    if not node:
        raise ValueError("Update Failed: node is invalid.")

    node.data = new_value
    return node

def update_value_at_position(dll, index, new_value):
    """
    Update the value at a given position in the linked list.
    :param dll: Doubly linked list object
    :param index: Zero-based index position in the list
    :param new_value: New value to assign
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Update Failed: linked list is empty.")

    target_node = dll.search_by_index(index)
    target_node.data = new_value
    return target_node

def replace_all_occurrences(dll, old_value, new_value):
    """
    Replace all occurrences of a value in the linked list.
    :param dll: Doubly linked list object
    :param old_value: Value to be replaced
    :param new_value: Replacement value
    :return: Number of nodes updated
    """
    if dll.is_empty():
        raise ValueError("Update Failed: linked list is empty.")

    curr_node = dll.head
    update_count = 0
    while curr_node:
        if curr_node.data == old_value:
            curr_node.data = new_value
            update_count += 1
        curr_node = curr_node.next

    return update_count

def swap_nodes(dll, node_a, node_b):
    """
    Swap two nodes in the linked list.
    :param dll: Doubly linked list object
    :param node_a: First node to swap
    :param node_b: Second node to swap
    :return: None
    """
    if dll.is_empty():
        raise ValueError("Swap Failed: linked list is empty.")

    # check if node1 and node 2 are same
    if node_a == node_b:
        print("Swap not needed, node1 and node 2 are same.")
        return

    adjacent_flag = (node_a.next == node_b) or (node_b.next == node_a)

    # check the order of nodes in dll (node_a <-> node_b or node_b <-> node_a)
    if node_b.next == node_a:
        node1, node2 = node_b, node_a
    else:
        node1, node2 = node_a, node_b

    # store neighbors for both of the nodes to maintain refs
    node1_next = node1.next
    node1_prev = node1.prev
    node2_next = node2.next
    node2_prev = node2.prev

    # swapping adjacent nodes
    if adjacent_flag:
        # check if node1 is head
        if node1_prev:
            node1_prev.next = node2
        else: # prev of node1 link is None -> head node
            dll.head = node2

        # check if node 2 is tail
        if node2_next:
            node2_next.prev = node1
        else: # next of node2 link is None -> tail node
            dll.tail = node1

        node1.next = node2_next
        node1.prev = node2

        node2.prev = node1_prev
        node2.next = node1
        return

    # swapping non adjacent nodes
    # check if Node 1 is head
    if node1_prev:
        node1_prev.next = node2
    else: # prev of node1 link is None -> head node
        dll.head = node2

    # check if Node 1 is tail
    if node1_next:
        node1_next.prev = node2
    else:
        dll.tail = node2

    # check if Node 2 is head
    if node2_prev:
        node2_prev.next = node1
    else:
        dll.head = node1
    # check if Node 1 is tail
    if node2_next:
        node2_next.prev = node1
    else:
        dll.tail = node1

    node2.prev = node1_prev
    node2.next = node1_next
    node1.prev = node2_prev
    node1.next = node2_next



def relink_nodes(dll, node1, node2):
    """
    Modify links between nodes without changing node data.
    This operation re-links nodes at the structural level only.
    :param dll: Doubly linked list object
    :param node1: First node involved in re-linking
    :param node2: Second node involved in re-linking
    :return: None
    """
    # Logic: detach node1 and insert before node2
    # ==================================================
    # Step 1: Detach node1
    # ==================================================
    if (node1 == node2) or (not node1) or (not node2):
        raise ValueError(
            "Relink Failed: either node1 and " 
            "node2 are same or one of them is None."
        )
    # Step D1: store neighbors of node1
    node1_next_neighbor, node1_prev_neighbor = node1.next, node1.prev

    # Step D2: update head and tail if node1 is at boundary
    if node1 == dll.head:
        dll.head = node1.next
    if node1 == dll.tail:
        dll.tail = node1.prev

    # Step D3: reconnect neighbors to keep list connected
    if node1_next_neighbor:
        node1_next_neighbor.prev = node1_prev_neighbor
    if node1_prev_neighbor:
        node1_prev_neighbor.next = node1_next_neighbor

    # Step D4: fully isolate node1
    node1.prev = None
    node1.next = None

    # ==================================================
    # Step 2: Insert node1 BEFORE node2
    # ==================================================
    # Step I0: store neighbors of node2
    node2_prev_neighbor = node2.prev

    # Step I1: link node1 to its new neighbors
    node1.next = node2
    node1.prev = node2_prev_neighbor
    node2.prev = node1

    # Step I2: link old neighbor of node2 forward
    if node2_prev_neighbor:
        node2_prev_neighbor.next = node1
    else:
        dll.head = node1


