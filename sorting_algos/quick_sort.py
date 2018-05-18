"""Quick Sort Algorithm"""


def quick_sort(lst):
    if len(lst) < 1:
        return lst

    pivot = lst[0]
    left = []
    middle = [pivot]
    right = []
    for i in range(1, len(lst)):
        if lst[i] <= pivot:
            left.append(lst[i])

        if lst[i] > pivot:
            right.append(lst[i])

    return quick_sort(left) + middle + quick_sort(right)
