"""Merge Sort Algorithm"""


def merge(lst_one, lst_two):
    
    new_lst = []

    while len(lst_one) > 0 and len(lst_two) > 0:

        if lst_one[0] < lst_two[0]:
            new_lst.append(lst_one[0])
            lst_one.remove(lst_one[0])

        else:
            new_lst.append(lst_two[0])
            lst_two.remove(lst_two[0])

    if len(lst_one) == 0:
        new_lst += lst_two

    else:
        new_lst += lst_one

    return new_lst


def merge_sort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst

    else:
        middle = len(lst) // 2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])

    return merge(left, right)
