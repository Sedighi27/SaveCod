a = 12
b = 12
c = 2022
print(a, b, c, sep="-")

print('A line of text.\n'.rstrip())

print(str(3.14))
print(None)

print('hello', 'world', sep=None)

print('hello', 'world', sep=' ')

print('hello', 'world')


print('hello', 'world', sep='\n')


print('/home', 'user', 'documents', sep='/')

print('', 'home', 'user', 'documents', sep='/')

print('line1\r\nline2\r\nline3')

print('Checking file integrity...', end='')
# (...)
print('ok')

print('Printing in a Nutshell', end='\n * ')
print('Calling Print', end='\n * ')
print('Separating Multiple Arguments', end='\n * ')
print('Preventing Line Breaks')

with open('file.txt') as file_object:
    for line in file_object:
        print(line)




