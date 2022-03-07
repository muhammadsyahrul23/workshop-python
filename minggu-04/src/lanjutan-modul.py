#mengimpor nama modul langsung ke tabel simbol modul impor
from fibo import fib, fib2
fib(500)

#mengimpor semua nama modul yang didefinisikan
from fibo import *
fib(500)

#ketikanama modul diikuti oleh as, maka nama setelah as terikat langsung ke modul yang diimpor
import fibo as fib
fib.fib(500)

#menggunakan from untuk mengimpor fibo dengan kegunaan yang sama seperti di atas
from fibo import fib as fibonacci
fibonacci(500)