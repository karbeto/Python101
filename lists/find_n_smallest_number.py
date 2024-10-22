my_list = [10, 7, 18, 5, 8, 14, 6, 10, 9, 15, 13, 20]

n = 3


def find_n_smallest_number(n, lst):
    lst.sort()
    print(lst)
    return lst[n]-1


print(find_n_smallest_number(n, my_list))
