raise NameError('HiThere')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: HiThere

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
An exception flew by!
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
NameError: HiThere