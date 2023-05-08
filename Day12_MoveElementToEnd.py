def move_element_to_end(array, element):
    """
    Receives an array and an element in the array and sends all instances of this element to the end of the array
    :param array:
    :param element:
    :return:
    """
    start, end = 0, len(array) - 1
    while start < end:
        while start < end and array[end] == element:
            end -= 1
        if array[start] == element:
            array[start], array[end] = array[end], array[start]
        start += 1
    return array
