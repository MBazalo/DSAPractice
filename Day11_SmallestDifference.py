def smallest_difference(ar1, ar2):
    """
    Given two arrays of integers return the two closest numbers from these two arrays.
    :param ar1: [int]
    :param ar2: [int]
    :return: list of two integers with the smallest difference [int]
    """
    ar1.sort()
    ar2.sort()
    i, j = 0, 0
    output = [ar1[i], ar2[j]]
    difference = float("inf")
    while i < len(ar1) and j < len(ar2):
        new_diff = abs(ar1[i] - ar2[j])
        if ar1[i] > ar2[j]:
            j += 1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar1[i] == ar2[j]:
            return output
        if new_diff < difference:
            difference = new_diff
            output = [ar1[i], ar2[j]]
    return output
