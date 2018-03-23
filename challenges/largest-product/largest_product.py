def largest_product(two_d_list):
    current_largest = 0
    for i in range(len(two_d_list)):
        product = two_d_list[i][0] * two_d_list[i][1]
        if current_largest < product:
            current_largest = product
    print(current_largest)


test_list = [[10, 10], [3, 4], [5, 6], [7, 8]]


largest_product(test_list)
