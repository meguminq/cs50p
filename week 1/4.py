exp = input('Expression: ')
x, y, z = exp.split(' ')

nx = float(x)
nz = float(z)

if y == '+':
    print(nx + nz)
elif y == '-':
    print(nx - nz)
elif y == '*':
    print(nx * nz)
elif y == '/':
    print(nx / nz)