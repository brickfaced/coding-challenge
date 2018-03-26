import largest_product as lp

sample_list_one = [[10, 10], [3, 4], [5, 6], [7, 8]]
sample_list_two = [[100, 10], [3, 4], [5, 6], [7, 8]]
sample_list_three = [[10, 10], [3, 1500], [5, 6], [7, 8]]


def test_largest_product():
    assert lp.largest_product(sample_list_one) == 100
    assert lp.largest_product(sample_list_two) == 1000
    assert lp.largest_product(sample_list_three) == 4500
