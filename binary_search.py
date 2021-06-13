def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while (left < right):
        mid = (left + right) // 2
        if target == mid:
            return mid
        elif target < mid:
            right = mid
        else:
            left = mid
    return None
