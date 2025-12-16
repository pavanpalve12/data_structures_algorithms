from double_linked_list.schemas import DoubleLinkedList, Node


def main():
    dll = DoubleLinkedList()
    values = [100, 200, 400, 500, 600, 100, 100, 200]
    dll.from_list(values)

    dll.delete_node(dll.search_by_value(500))
    dll.print_linked_list()

if __name__ == "__main__":
    main()