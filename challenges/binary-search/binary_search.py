def binary_search(sorted_list, search_key):
    for i in range(len(sorted_list)):
        if sorted_list[i] == search_key:
            return i
    return -1
