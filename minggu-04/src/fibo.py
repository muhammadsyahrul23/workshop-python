# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#memasukkan interpreter python dan mengimpor modul
import fibo

#memasukkan nama modul fibo, menggunakan nama modul dan mengakses fungsi
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

#menetapkan fungsi ke nama lokal
fib = fibo.fib
fib(500)