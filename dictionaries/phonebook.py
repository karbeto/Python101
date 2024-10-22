phonebook = {}


def add_contact(name, number):
    phonebook[name] = number


def remove_contact(name):
    if (name in phonebook):
        del phonebook[name]
    else:
        print('There is no contact with that name')


def search_contacts(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print('There is no contact with that name')


add_contact('Kristijan', '7752458')
add_contact('Hristijan', '7752458')
add_contact('Antonio', '075245899')
add_contact('Sashe', '075245282')
print(phonebook)

remove_contact('Hristijan')
print(phonebook)

search_contacts('Kristijan')
