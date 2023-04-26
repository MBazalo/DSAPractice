def single_number(array):
    """
    Takes in an array of integers with only a single number not repeated. Finds that number and returns it.
    Using O(n) time and O(1) space complexities.
    :param array: List[int]
    :return: int
    """
    # Using bitwise xor, when a number is repeated (number ^ same number will evaluate to zero).
    xor = 0
    for number in array:
        xor ^= number
    return xor
