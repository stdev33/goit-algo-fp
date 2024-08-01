from linked_list import LinkedList


def main():
    list1 = LinkedList()
    list1.insert_at_end(10)
    list1.insert_at_end(30)
    list1.insert_at_end(50)

    list2 = LinkedList()
    list2.insert_at_end(20)
    list2.insert_at_end(40)
    list2.insert_at_end(60)

    # Test reverse method
    list1.reverse()
    list1.print_list()  # Output: 50 -> 30 -> 10
    print()

    # Test insertion_sort method
    list1.insertion_sort()
    list1.print_list()  # Output: 10 -> 30 -> 50
    print()

    # Test merge_sorted_lists method
    list1.merge_sorted_lists(list2)
    list1.print_list()  # Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60
    print()

if __name__ == "__main__":
    main()