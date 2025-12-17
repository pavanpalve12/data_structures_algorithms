from double_linked_list.schemas import DoubleLinkedList, Node


def main():
    dll = DoubleLinkedList()
    values = [100, 200, 400, 500, 600]
    dll.from_list(values)
    dll.print_linked_list()
"""
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400)

    n1.next = n2
    n2.next = n3
    n3.next = n1
    n4.next = None

    n1.prev = None
    n2.prev = n1
    n3.prev = n2
    n4.prev = n3

    dll.head = n1
    dll.tail = n4
"""


if __name__ == "__main__":
    main()