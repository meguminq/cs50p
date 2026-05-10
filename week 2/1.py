u = ''
camel_case = input('camel case: ')
for c in camel_case:
    if c.isupper() == False:
        u += c
    else:
        u += '_' + c.lower()
print('snake_case:', u)