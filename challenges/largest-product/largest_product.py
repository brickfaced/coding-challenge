def largest_product(two_d_list):
    if isinstance(two_d_list, list) is False:
        raise TypeError('Make sure you inputted a list')

    current_largest = 0

    for i in range(len(two_d_list)):
        if isinstance(two_d_list[i][0], int) is False:
            raise TypeError('Make sure your list only contains integers')        

        if isinstance(two_d_list[i][1], int) is False:
            raise TypeError('Make sure your list only contains integers')

        product = two_d_list[i][0] * two_d_list[i][1]

        if product > current_largest:
            current_largest = product

    return(current_largest)
