"""Radix Sort Algorithm"""


def radix_sort(lst, radix=10):
    """
    Set initial values for temp and placement.
    """
    max_length = False
    temp, placement = -1, 1

    while max_length is False:
        max_length = True
        """
        Instantiate buckets for each number
        in the radix(0-9) where it will place each
        value in the list based on the number of the
        current digit.
        """
        buckets = [list() for _ in range(radix)]

        for i in lst:
            """
            For each value in the last it's
            going to set temp as the value divided
            by the current placement value and then set
            append the value at the index of temp % radius.
            IE:
            100 // 1 = 100
            buckets[100 % 10 = 0].append(100)
            """
            temp = i // placement
            buckets[temp % radix].append(i)
            if max_length is True and temp > 0:
                max_length = False

        counter = 0

        for bucket in range(radix):
            """
            Here we iterate through each bucket
            """
            for i in buckets[bucket]:
                """
                Here we iterate through the bucket and start setting
                the values in the list equal to the the current item in the
                bucket and then increment counter to go to the next index
                """
                lst[counter] = i
                counter += 1
        """
        Multiply placement by radix to get into the next digit in the values
        of the list and repeat process until Max Length = True
        """
        placement *= radix

    return lst
