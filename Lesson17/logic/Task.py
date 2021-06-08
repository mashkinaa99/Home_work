# Lesson 13, Task 3
def number_list(nums: list):
    return nums


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    neg = []
    for num in nums:
        if num < 0:
            neg.append(num)
    if len(neg) < 1:
        def filter_pos():
            return func1(nums)

        return filter_pos

    else:
        def filter_neg():
            return func2(nums)

        return filter_neg


c = number_list([1, 2, 3, 4, -10])
d = number_list([1, -5, 3, 4, -10])

a = choose_func(c, square_nums, remove_negatives)

b = choose_func(d, square_nums, remove_negatives)
