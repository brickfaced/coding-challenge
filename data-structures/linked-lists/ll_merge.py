def merge_lists(ll_one, ll_two):
    current_one = ll_one.head
    current_two = ll_two.head

    while current_one and current_two:
        temp = current_two._next

        if not current_one._next:
            current_one._next = current_two
            break

        current_two._next = current_one._next
        current_one._next = current_two
        current_one = current_two._next
        current_two = temp

    ll_one._size += ll_two._size
    return 'Successfully merged into first Linked List'
