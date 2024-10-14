my_list = [1, 2, 3]

d = {i: 'a' for i in range(1, 11)}
print(d)


dictionary = {i: i+10 for i in my_list}
print(dictionary)

odds = []

for i in range(0, 10):
    if i % 2 == 0:
        odds.append(i+10)

print(odds)

odds = [i+10 for i in range(0, 10) if i % 2 == 0]
print(odds)
