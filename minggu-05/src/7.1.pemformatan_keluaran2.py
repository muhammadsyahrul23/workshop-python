#menggunakan fungsi str() dan repr() yang memiliki representasi sama
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

#output
'Hello, world.'
"'Hello, world.'"
'0.14285714285714285'
'The value of x is 32.5, and y is 40000...'
'hello, world\n'
"(32.5, 40000, ('spam', 'eggs'))"