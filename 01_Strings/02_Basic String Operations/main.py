# len('hi there!')
print(len('hi there!'))

# len('')
print(len(''))

# print('hi there!'[1])
print(len(' '))

# print('hi there!'[1:])
print('hi there!'[1])

# print('hi there!'[:5])
print('hi there!'[1:])

# print('hi there!'[3:6])
print('hi there!'[:5])

# print('I\'m Adrian')
print('hi there!'[3:6])

# ord('a')
print('I\'m Adrian')
print("\"I'm Adrian\"")
print('"I\'m Adrian"')

# ord('A')
# \t is the horizontal tab
# \n is the new line 
# \r is the return the cursor to the left 
# \\ is the single backslash

print(ord('a'))

# chr(97)
print(ord('A'))
print(ord('🥶'))

# test_string = '''Line 1
# Line 2'''
print(chr(97))

# len(test_string)
print(chr(256))

# 'aaa' + 'bbb'
print(chr(128512))

# 2 * 'ccc'
test_string = '''Line 1
Line 2
Line 3'''

# for char in 'hello from the world of Python':
#     print(char, end='-')
print(len(test_string))
print(test_string)

print('aaa' + 'bbb')

print(2 * 'ccc')

for char in 'hello from the world of Python':
    print(char, end='-')

print()
# text = 'dHello there!'
# del text[0]

# min('ilovetravellingaroundtheworld')
print(min('ilovetravellingaroundtheworld'))

print(min('i love travellingaroundtheworld'))

# min('i love travellingaroundtheworld')
print(max('ilovetravellingaroundtheworld'))

# max('ilovetravellingaroundtheworld')
for i in range(100000, 150000):
    print(chr(i), end=" ")
