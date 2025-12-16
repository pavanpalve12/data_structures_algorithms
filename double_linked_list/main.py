from double_linked_list.schemas import DoubleLinkedList, Node


def main():
    dll = DoubleLinkedList()

    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(300)
    n5 = Node(300)

    n1.next = n2
    n1.prev = None
    n2.next = n3
    n2.prev = n1
    n3.next = n4
    n3.prev = n2
    n4.next = n5
    n4.prev = n3
    n5.next = None
    n5.prev = n4

    dll.head = n1
    dll.tail = n3

    curr_node = dll.head
    while curr_node:
        print(f"{curr_node.data}", end=" -> ")
        curr_node = curr_node.next

    print(dll.is_empty())
    print(dll.traverse())

    dll.print_linked_list()

    print(dll.clear())

if __name__ == "__main__":
    main()