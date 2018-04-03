from linked_list import LinkedList as LL
from node import Node


def merge_lists(ll_one, ll_two):
    current_one = ll_one.head
    current_two = ll_two.head

    if len(ll_two) > len(ll_one):
        current_one = ll_two.head
        current_two = ll_one.head

    while current_two is not None:
        ll_one.insert_after(current_one.val, current_two.val)
        current_one = current_one._next._next
        current_two = current_two._next

    return ll_two
