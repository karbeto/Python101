my_list = [2, 1, 3, 5, 7, 6]
res_list = []

i = len(my_list) - 1
while i >= 0:
    res_list.append(my_list[i])
    i = i - 1

print(res_list)
