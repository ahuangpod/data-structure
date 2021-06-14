def merge_sort(lst):
    merge_sort_helper(lst, 0, len(lst)-1)


def merge_sort_helper(lst, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(lst, left, mid)
        merge_sort_helper(lst, mid+1, right)
        merge(lst, left, mid, right)


def merge(lst, left, mid, right):
    left_lst = lst[left:mid+1]
    right_lst = lst[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] < right_lst[j]:
            lst[k] = left_lst[i]
            i += 1
        else:
            lst[k] = right_lst[i]
            j += 1
        k += 1
