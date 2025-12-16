from double_linked_list.schemas import DoubleLinkedList, Node


def main():
    dll = DoubleLinkedList()
    values = [100, 200, 400, 500, 600]
    dll.from_list(values)
    dll.print_linked_list()

    dll.update_node_value(dll.search_by_value(200), 250).data
    dll.print_linked_list()

    dll.update_value_at_position(2, 450).data
    dll.print_linked_list()

if __name__ == "__main__":
    main()