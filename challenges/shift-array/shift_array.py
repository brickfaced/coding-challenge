def insert_shift_array(array, insert_int):
    length = len(array) + 1
    new_array = [None] * length
    middle_index = len(new_array) // 2
    for i in range(length):
        if i < middle_index:
            new_array[i] = array[i]
        if i == middle_index:
            new_array[i] = insert_int
        elif i > middle_index:
            new_array[i] = array[i - 1]
    return new_array

insert_shift_array([4, 8, 15, 23, 42], 16)
insert_shift_array([2, 4, 6, 8], 5)
