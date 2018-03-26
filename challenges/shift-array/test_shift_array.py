import shift_array as sa


def test_shift_array():
    """
    Test to see if works with odd or even number indexes
    """
    assert sa.insert_shift_array([4, 8, 15, 23, 42], 16) ==\
        [4, 8, 15, 16, 23, 42]
    assert sa.insert_shift_array([2, 4, 6, 8], 5) == [2, 4, 5, 6, 8]