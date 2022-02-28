#tuples beserta urutan sequences
t = 12345, 54321, 'hello!'
t[0]
t
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# Tuples are immutable:
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v 

#Tuple kosong dibangun oleh sepasang kurung kosong;
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
len(singleton)
singleton
x, y, z = t