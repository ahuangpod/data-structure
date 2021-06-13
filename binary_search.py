def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while (left < right):
        mid = (left + right) // 2
        if target == lst[mid]:
            return mid
        elif target < mid:
            right = mid
        else:
            left = mid
    return None

print(binary_search([1,2,3,4,5], 3))
