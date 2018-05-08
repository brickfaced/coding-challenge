"""Selection Sort Algorithm"""


def selection_sort(lst):
    """
    Input an lst and have it sorted using the selection method
    """
    if len(lst) < 2:
        return lst

    for i in range(len(lst)):
        min_pos = i
        for j in range(i+1, len(lst)):
            if lst[min_pos] > lst[j]:
                min_pos = j

        temp = lst[i]
        lst[i] = lst[min_pos]
        lst[min_pos] = temp

    return lst
