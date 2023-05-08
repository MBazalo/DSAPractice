
# Finding two numbers that add up to a given target sum

def two_sum(array, target):
    numbers = dict()
    for number in array:
        if target - number in numbers:
            return [target - number, number]
        else:
            numbers[number] = True
