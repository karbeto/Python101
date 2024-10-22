my_set = {'apple', 'samsung', 'xiaomi', 'huawei'}
another_set = set(('apple', 'samsung', 'xiaomi', 'huawei'))

print(type(my_set))

print('samsung' in another_set)

my_set.add('lenovo')

print(my_set)
my_set.remove('lenovo')
print(my_set)

new_set = {'Asus', 'Lenovo', 'Poco', 'BlackView'}

my_set.update(new_set)
print(my_set)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# Union
set3 = set1 | set2
print(set3)

set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}

# Intersection
set6 = set4 & set5
print(set6)

# Difference will keep all items from first set that are not in second
set7 = set4 - set5
print(set7)

# Symmetric Differences will keep only the elements that are
# NOT present in both sets
set8 = set4 ^ set5
print(set8)
