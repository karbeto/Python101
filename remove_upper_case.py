my_string = 'ThIs Is My StRIng WiTH uPPer cAsE'

without = ''.join([elem for elem in my_string if not elem.isupper()])

print(my_string)
print(without)
