data = ['Volkswagen', 50, 22000, (2017, 12, 21)]
name, shares, price, (year, mon, day) = data

print(name)
print(year)

s = 'Hello'
a, b, c, d, e = s

print(a)
print(e)

data = ('John', 'Doe', 'johndoe@example.com', '075-555-1212', '075-777-1312')

name, surname, email, *phone_numbers = data

print(name)
print(email)
print(phone_numbers)
