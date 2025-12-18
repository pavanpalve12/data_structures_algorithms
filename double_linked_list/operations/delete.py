"""
------------------------------------------------------------------------------------
Module: Doubly Linked List Deletion Operations
------------------------------------------------------------------------------------
This module defines deletion operations for a doubly linked list.
Each function removes nodes while preserving list integrity and
maintaining valid bidirectional links.
------------------------------------------------------------------------------------
Available Functions:
    - delete_from_head(dll)
    - delete_from_tail(dll)
    - delete_at_index(dll, index)
    - delete_node(dll, target_node)
    - delete_by_value(dll, value)
    - delete_before_node(dll, target_node)
    - delete_after_node(dll, target_node)
    - delete_all_occurrences(dll, value)
    - clear(dll)
------------------------------------------------------------------------------------
"""


def delete_from_head(dll):
    """
    Function: Delete the first node (head) of the linked list
    :param dll: Doubly linked list instance
    :return: Deleted node if successful, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Delete from head failed: the linked list is empty.")

    deleted_head = dll.head
    if dll.head == dll.tail:
        dll.head = dll.tail = None
        return deleted_head

    new_head = deleted_head.next
    new_head.prev = None
    dll.head = new_head

    deleted_head.next = None
    deleted_head.prev = None
    return deleted_head

def delete_from_tail(dll):
    """
    Function: Delete the last node (tail) of the linked list
    :param dll: Doubly linked list instance
    :return: Deleted node if successful, otherwise None
    """
    # 100 - 200 - 300
    # 100
    if dll.is_empty():
        raise ValueError("Delete from tail failed, the linked list is empty.")

    deleted_tail = dll.tail

    if dll.tail == dll.head:
        dll.tail = dll.head = None
        return deleted_tail

    new_tail = deleted_tail.prev
    new_tail.next = None
    dll.tail = new_tail

    deleted_tail.next = deleted_tail.prev = None
    return deleted_tail

def delete_at_index(dll, index):
    """
    Function: Delete a node at a specific index
    :param dll: Doubly linked list instance
    :param index: Zero-based position of the node to delete
    :return: Deleted node if successful, otherwise None
    """
    target_node = dll.search_by_index(index)

    if target_node == dll.head:
        return dll.delete_from_head()
    if target_node == dll.tail:
        return dll.delete_from_tail()

    prev_node = target_node.prev
    next_node = target_node.next

    prev_node.next = next_node
    next_node.prev = prev_node
    target_node.next = None
    target_node.prev = None

    return target_node

def delete_node(dll, target_node):
    """
    Function: Delete a specific node using direct reference
    :param dll: Doubly linked list instance
    :param target_node: Node to be deleted
    :return: Deleted node if successful, otherwise None
    """
    if dll.is_empty():
        raise ValueError("Delete node failed, the linked list is empty.")

    if target_node == dll.head:
        return dll.delete_from_head()
    if target_node == dll.tail:
        return dll.delete_from_tail()

    prev_node = target_node.prev
    next_node = target_node.next

    prev_node.next = next_node
    next_node.prev = prev_node
    target_node.next = None
    target_node.prev = None

    return target_node

def delete_by_value(dll, value):
    """
    Function: Delete the first occurrence of a value
    :param dll: Doubly linked list instance
    :param value: Value of the node to delete
    :return: Deleted node if found, otherwise None
    """
    target_node = dll.search_first_occurrence(value)
    return dll.delete_node(target_node)

def delete_before_node(dll, target_node):
    """
    Function: Delete the node immediately before a given node
    :param dll: Doubly linked list instance
    :param target_node: Node whose previous node will be deleted
    :return: Deleted node if successful, otherwise None
    """
    if target_node.prev:
        node_before = target_node.prev
        return dll.delete_node(node_before)
    return None

def delete_after_node(dll, target_node):
    """
    Function: Delete the node immediately after a given node
    :param dll: Doubly linked list instance
    :param target_node: Node whose next node will be deleted
    :return: Deleted node if successful, otherwise None
    """
    if target_node.next:
        node_after = target_node.next
        return dll.delete_node(node_after)
    return None

def delete_all_occurrences(dll, value):
    """
    Function: Delete all nodes containing a given value
    :param dll: Doubly linked list instance
    :param value: Value to remove from the list
    :return: Number of nodes deleted
    """
    if dll.is_empty():
        raise ValueError("Delete all occurrences failed: the linked list is empty.")

    deleted_count = 0
    curr_node = dll.head
    while curr_node:
        next_node = curr_node.next

        if curr_node.data == value:
            dll.delete_node(curr_node)
            deleted_count += 1

        curr_node = next_node

    return deleted_count

def delete_all_nodes(dll):
    """
    Function: Delete all nodes from the linked list
    :param dll: Doubly linked list instance
    :return: True if the list is cleared successfully, otherwise False
    """
    dll.clear()
