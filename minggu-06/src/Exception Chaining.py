raise RuntimeError from exc
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

Traceback (most recent call last):
    File "<stdin>", line 4, in <module>
RuntimeError