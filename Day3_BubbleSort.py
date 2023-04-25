def bubble_sort(array):
    swaps = 0
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            swaps += 1
    if swaps:
        bubble_sort(array)
