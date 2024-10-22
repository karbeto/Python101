num = []
for i in range(0, 10):
    num.append(i+10)
print(num)

numbers = [i+10 for i in range(0, 10)]
print(numbers)

my_list = list(range(10, 20, 1))
print(my_list)

a = [i % 2 for i in range(0, 10)]
print(a)
