def three_number_sum(ar, target_sum):
    """
    Given an array with unique integers and a target sum, this function returns all unique triplets that sum to that
    target sum.
    :param ar:
    :type ar: [int]
    :param target_sum:
    :type target_sum: int
    :return: [[int]]
    """
    output = []
    ar.sort()
    for i in range(len(ar) - 2):
        number = ar[i]
        new_target = target_sum - number
        start = i + 1
        end = len(ar) - 1
        while start < end:
            if ar[end] + ar[start] == new_target:
                output.append([number, ar[start], ar[end]])
                end -= 1
                start += 1
            elif ar[end] + ar[start]> new_target:
                end -= 1
            else:
                start += 1
    return output
