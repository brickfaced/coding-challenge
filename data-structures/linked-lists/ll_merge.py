from linked_list import LinkedList as LL
from node import Node


def merge_lists(ll_one, ll_two):
    current_one = ll_one.head
    current_two = ll_two.head
    cache_one = current_one._next
    cache_two = current_two._next
    while current_one._next:
     current_one._next = current_two
