s = 'Hello, world.'
str(s)
# 'Hello, world.' (Output)
repr(s)
# "'Hello, world.'" (Output)
str(1/7)
# '0.14285714285714285' (Output)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000... (Output)

# Repr() dari sebuah string menambahkan tanda kutip string dan garis miring terbalik:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# 'hello, world\n' (Output)

# Argumen untuk repr() dapat berupa objek Python apa pun:
repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))" (Output)