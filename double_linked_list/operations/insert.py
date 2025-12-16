"""
------------------------------------------------------------------------------------
Module: Doubly Linked List Insertion Operations
------------------------------------------------------------------------------------
This module defines insertion operations for a doubly linked list.
Each function handles a specific insertion strategy while preserving
list integrity and bidirectional links.
------------------------------------------------------------------------------------
Available Functions:
    - insert_at_head(dll, value)
    - insert_at_tail(dll, value)
    - insert_at_index(dll, index, value)
    - insert_before_node(dll, target_node, value)
    - insert_after_node(dll, target_node, value)
    - insert_before_value(dll, target_value, value)
    - insert_after_value(dll, target_value, value)
    - insert_sorted(dll, value)
------------------------------------------------------------------------------------
"""

def insert_at_head(dll, new_node):
    """
    Function: Insert a new node at the beginning of the linked list
    :param dll: Doubly linked list instance
    :param new_node: new_node
    :return: None
    """
    if dll.is_empty():
        print(f"Linked list is empty: node {new_node.data} added at head.")
        dll.head = dll.tail = new_node
    else:
        print(f"Node {new_node.data} added before head {dll.head.data}.")
        new_node.next = dll.head
        dll.head.prev = new_node
        dll.head = new_node

def insert_at_tail(dll, new_node):
    """
    Function: Insert a new node at the end of the linked list
    :param dll: Doubly linked list instance
    :param new_node: new_node to be inserted
    :return: None
    """
    # 100 200 300 ---  100 200 300 400 -> tail
    # 400: ... <- 300 -> 400, 300 <- 400 -> None
    if dll.is_empty():
        print(f"Linked list is empty: node {new_node.data} added at head.")
        dll.head = dll.tail = new_node
    else:
        print(f"Node {new_node.data} added after tail {dll.tail.data}.")
        new_node.prev = dll.tail
        dll.tail.next = new_node
        dll.tail = new_node

def insert_at_index(dll, index, new_node):
    """
    Function: Insert a new node at a specific index
    :param dll: Doubly linked list instance
    :param index: Zero-based position for insertion
    :param new_node: new_node to be inserted
    :return: None
    """
    target_node = dll.search_by_index(index)

    if target_node == dll.head:
        dll.insert_at_head(new_node.data)
    else:
        prev_node = target_node.prev

        new_node.next = target_node
        new_node.prev = prev_node

        prev_node.next = new_node
        target_node.prev = new_node

def insert_before_node(dll, target_node_value, new_node):
    """
    Function: Insert a new node before a given node
    :param dll: Doubly linked list instance
    :param target_node_value: Node before which insertion occurs
    :param new_node: new_node to be inserted
    :return: None
    """
    target_node = dll.search_by_value(target_node_value)

    if target_node == dll.head:
        dll.insert_at_head(new_node.data)
    else:
        prev_node = target_node.prev

        new_node.next = target_node
        new_node.prev = prev_node

        prev_node.next = new_node
        target_node.prev = new_node

def insert_after_node(dll, target_node_value, new_node):
    """
    Function: Insert a new node after a given node
    :param dll: Doubly linked list instance
    :param target_node_value: Node after which insertion occurs
    :param new_node: new_node to be inserted
    :return: None
    """
    target_node = dll.search_by_value(target_node_value)

    if target_node == dll.tail:
        dll.insert_at_tail(new_node.data)
    else:
        next_node = target_node.next

        new_node.next = next_node
        new_node.prev = target_node

        next_node.prev= new_node
        target_node.next = new_node

def insert_before_value(dll, target_value, new_node):
    """
    Function: Insert a new node before the first occurrence of a value
    :param dll: Doubly linked list instance
    :param target_value: Value before which insertion occurs
    :param new_node: new_node to be inserted
    :return: None
    """
    target_node = dll.search_first_occurrence(target_value)

    if target_node == dll.head:
        dll.insert_at_head(new_node.data)
    else:
        prev_node = target_node.prev

        new_node.next = target_node
        new_node.prev = prev_node
        prev_node.next = new_node
        target_node.prev = new_node

def insert_after_value(dll, target_value, new_node):
    """
    Function: Insert a new node after the first occurrence of a value
    :param dll: Doubly linked list instance
    :param target_value: Value after which insertion occurs
    :param new_node: new_node to be inserted
    :return: None
    """
    target_node = dll.search_first_occurrence(target_value)

    if target_node == dll.tail:
        dll.insert_at_tail(new_node.data)
    else:
        next_node = target_node.next

        new_node.next = next_node
        new_node.prev = target_node
        target_node.next = new_node
        next_node.prev = new_node

def insert_sorted_ascending(dll, new_node):
    """
    Function: Insert a new node while maintaining ascending sorted order
    :param dll: Doubly linked list instance
    :param new_node: new_node to be inserted
    :return: None
    """

    if dll.is_empty():
        dll.insert_at_head(new_node.data)
        return

    curr_node = dll.head
    while curr_node and curr_node.data < new_node.data:
        curr_node = curr_node.next

    if curr_node is None:
        dll.insert_at_tail(new_node.data)
        return

    if curr_node == dll.head:
        dll.insert_at_head(new_node.data)
        return

    prev_node = curr_node.prev

    new_node.next = curr_node
    new_node.prev = prev_node

    prev_node.next = new_node
    curr_node.prev = new_node

def insert_sorted_descending(dll, new_node):
    """
    Function: Insert a new node while maintaining descending sorted order
    :param dll: Doubly linked list instance
    :param new_node: new_node to be inserted
    :return: None
    """
    if dll.is_empty():
        dll.insert_at_head(new_node.data)
        return

    curr_node = dll.head
    while curr_node and curr_node.data > new_node.data:
        curr_node = curr_node.next

    if curr_node is None:
        dll.insert_at_tail(new_node.data)
        return

    if curr_node == dll.head:
        dll.insert_at_head(new_node.data)
        return

    prev_node = curr_node.prev

    new_node.next = curr_node
    new_node.prev = prev_node

    curr_node.prev = new_node
    prev_node.next = new_node