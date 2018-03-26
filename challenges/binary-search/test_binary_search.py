import binary_search as bs


def test_binary_search():
    assert bs.binary_search([4, 8, 15, 16, 23, 42], 15) == 2
    assert bs.binary_search([4, 8, 15, 16, 23, 42], 17) == -1
