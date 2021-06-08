nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


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


a = choose_func(nums1, square_nums, remove_negatives)

b = choose_func(nums2, square_nums, remove_negatives)

assert a() == [1, 4, 9, 16, 25]

assert b() == [1, 3, 5]
