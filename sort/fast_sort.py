def partition(lst, left, right):
    pivot_index = left
    pivot = lst[left]
    left += 1
    while (left < right):
        if lst[left] > pivot and lst[right] < pivot:
            tmp = lst[left]
            lst[left] = right
            lst[right] = tmp
        if lst[left] <= pivot:
            left += 1
        elif lst[right] >= pivot:
            right -= 1

    lst[pivot_index] = lst[left]
    lst[left] = pivot
    return left


def fast_sort(lst, left, right):
    if left < right:
        pivot_index = partition(lst, left, right)
        fast_sort(lst, left, pivot_index-1)
        fast_sort(lst, pivot_index+1, right)


lst = [10,34,1,6,43,78]
fast_sort(lst, 0, len(lst)-1)
print(lst)
