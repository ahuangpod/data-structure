def selection_sort(lst):
    sorted_lst = []
    max_index = len(lst) -1
    i = 0
    while (i < max_index):
        j = i
        min = lst[j]
        while (j < max_index):
            if lst[j] < min:
                min = lst[j]
            j += 1
        sorted_lst.append(min)
        i += 1
    return sorted_lst

print(selection_sort([3,5,6,1,2,3,5,10]))
