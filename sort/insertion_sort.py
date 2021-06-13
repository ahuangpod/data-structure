def insertion_sort(lst):
    i = 1
    n = len(lst) - 1
    while i < n:
        j = i - 1
        item_to_insert = lst[i]
        while j >= 0:
            if lst[j] < item_to_insert:
                break
            else:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
                j -= 1

        i += 1
    return lst


print(insertion_sort([5,1,7,2,9,34]))
