def bubble_sort(lst):
    n = len(lst) - 1
    while (n > 0):
        i = 0
        while i < n:
            if lst[i] > lst[i+1]:
                tmp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = tmp
            i += 1
        n -= 1
    return lst


print(bubble_sort([4,1,7,9,2,32]))
