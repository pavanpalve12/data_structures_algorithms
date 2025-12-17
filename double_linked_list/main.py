from double_linked_list.schemas import DoubleLinkedList, Node


def main():
    dll1 = DoubleLinkedList()
    values = "Z B D T U P".split(" ")
    dll1.from_list(values)
    dll1.print_linked_list()

    dll1.sort_ascending()
    dll1.print_linked_list()

    dll1.sort_descending()
    dll1.print_linked_list()

if __name__ == "__main__":
    main()

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