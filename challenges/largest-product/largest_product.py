def largest_product(two_d_list):
    current_largest = 0
    for i in range(len(two_d_list)):
        product = two_d_list[i][0] * two_d_list[i][1]
        if product > current_largest:
            current_largest = product
    return(current_largest)
