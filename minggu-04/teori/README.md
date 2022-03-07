# BAB 6
# Modules

---

Jika kita berhenti dari interpreter python dan memasukkannya lagi, definisi yang kita buat (fungsi atau variabel) akan hilang. Karena itu, jika kita ingin menulis program yang agak lebih pajang, kita lebih baik menggunakan editor teks untuk menyiapkan input bagi penerjemah dan menjalankannya dengan file itu sebagai input atau juga dikenal dengan pembuatan script. Saat program kita menjadi lebih panjang, kita mungkin ingin membaginya menjadi beberapa file untuk pengelolaan yang lebih mudah agar praktis ketika meuliskan beberapa progam tanpa menyalin definisi di setiap prgram.

Untuk mendukung ini, Python memiliki cara untuk meletakkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter. File ini disebut dengan Module. 

Module pada Python adalah sebuah file yang berisikan sekumpulan kode fungsi, class dan variabel yang disimpan dalam satu file berekstensi `.py` dan dapat dieksekusi oleh interpreter Python. Nama dari module `.py` merupakan nama nama dari file itu sendiri. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global `__name__.` Misalnya, gunakan editor teks favorit Anda untuk membuat bernama bernama `fibo.py` di direktori saat ini dengan konten berikut

```python
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
```

Kemudian masuk ke dalam interpreter Python dan import modul ini dengan perintah berikut

```python
>>> import fibo
```

Dalam hal ini, kita tidak memasukkan nama fungsi yang didefinisikan dalam `fibo` secara langsung dalam table simbol saat ini. Kita hanya memasukkan nama modul di sini dan menggunakan nama modul kita dapat mengakses fungsi:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Jika kita sering ingin menggunakan suatu fungsi, kita dapat menetapkannya ke nama lokal seperti:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

**6.1. More on Modules / Lebih lanjut tentang Modul**

---

Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul.

Modyl akan dieksekusi hanya pertama kali ketika nama modul ditemui dalam pernyataan import. Setiap modul memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, penulis modul dapat menggunakan variabel global dalam modul tanpa khawatir tentang bentrokan tidak disengaja dengan variabel global pengguna. kita dapat menggunakan variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, seperti `modname.itemname`.

Kemudian juga modul dapat mengimport modul lain. Tetapi tidak diperlukan untuk menempatkan semua pernyataan import di awal modul (atau skrip). Nama-nama modul yang diimport ditempatkan pada tabel simbol global modul import. Ada varian dari pernyataan `import` yang mengimport nama dari modul langsung ke tabel simbol modul import seperti:

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Dalam pernyataan di atas tidak memperkenalkan nama modul dari mana import diambil dalam tabel simbol lokal, seperti pada contoh di atas `fibo` tidak didefinisikan.

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Pernyataan di atas akan mengimport semua nama kecuali yang dimulai dengan garis bawah `(_)`. Dalam kebanyakan kasus, programmer Python tidak menggunakan fasilitas ini karena ia memperkenalkan sekumpulan nama yang tidak diketahui ke dalam interpreter, mungkin menyembunyikan beberapa hal yang sudah kita definisikan.

Perhatikan bahwa secara umum praktik mengimpor `*` dari modul atau paket tidak disukai, karena sering menyebabkan kode yang kurang dapat dibaca. Namun, boleh saja menggunakannya untuk menghemat pengetikan di sesi interaktif.

Jika nama modul diikuti oleh `as`, maka nama setelah `as` terikat langsung ke modul yang diimport.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Dalam pertanyaan di atas secara efektif mengimpor modul dengan cara yang sama dengan `import fibo` yang akan dilakukan, dengan satu-satunya perbedaan adalah sebagai `fib`.

Hal tersebut juga dapat digunakan ketika menggunakan `from` yakni:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

`Catatan: Untuk alasan efisiensi, setiap modul hanya diimport satu kali per sesi interpreter. Oleh karena itu, jika kita mengubah modul, kita harus memulai ulang interpreter. Atau jika hanya satu modul yang ingin kita uji secara interaktif, dapat menggunakan importlib.reload() Contohnya import importlib; importlib.reload(modulename).`

**6.1.1. Executing modules as scripts / Mengoperasikan modul sebagai skrip**

---

Ketika kita mengoprasikan modul Python dengan `python fibo.py <arguments>`, kode dalam modul akan dieksekusi. Sama seperti jika kita mengimportnya tetapi dengan `__name__` yang diatur ke `__main__`. Itu berarti bahwa dengan menambahkan kode tersebut di akhir modul.

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Kita dapat membuat berkas dapat digunakan sebagai skrip dan juga modul yang dapat diimport, karena kode yang mengurai parsing baris perintah hanya beroperasi jika modul dieksekusi sebagai berkas `main`. dengan mengeksekusi perintah:

```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

Jika modul diimport, kode tersebut tidak bisa dieksekusi:

```python
>>> import fibo
>>>
```

**6.1.2. The Module Search Path / Jalur Pencarian Modul**

---

Ketika sebuah modul bernama `spam` diimport, interpreter pertama-tama akan mencari modul bawaan dengan nama itu. Jika tidak ditemukan, maka kemudian akan mencari berkas bernama spam.py dalam daftar directory yang diberikan oleh variabel `sys.path. sys.path` yang diinisialisasi dari lokasi ini:
  * Directory yang berisi script masukan (atau direktori saat ini ketika tidak ada file ditentukan).
  * PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan variabel shell PATH).
  * The installation-dependent default (by convention including a site-packages directory, handled by the site module).

`Catatan: Pada sistem file yang mendukung symlink, directory yang berisi script masukan dihitung setelah symlink diikuti. Dengan kata lain directory yang berisi symlink (tidak) ditambahkan ke jalur pencarian modul.`

Setelah inisialisasi, program Python dapat memodifikasi ` data :sys.path`. Directory yang berisi script yang dijalankan dan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. Ini berarti bahwa script dalam directory itu akan dimuat bukan modul dengan nama yang sama di directory pustaka. Hal tersebut adalah kesalahan kecuali penggantian memang diharapkan.

**6.1.3. “Compiled” Python files / Berkas Python "Compiled"**

---

Untuk mempercepat memuat modul, Python menyimpan cache versi terkompilasi dari setiap modul di directory `__pycache__` dengan nama `module. version.pyc`, di mana versi menyandikan format berkas terkompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi yang dikompilasi dari `spam.py` akan di-cache sebagai `__pycache__/spam.cpython-33.pyc`. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang beragam dan versi Python yang berbeda.

Python memeriksa tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat apakah itu kedaluwarsa dan perlu dikombinasi ulang. Hal tersebut adalah proses yang sepenuhnya otomatis. selain itu juga modul yang dikombinasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Di sisi lain Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, itu tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (dikompilasi saja), modul yang dikompilasi harus ada di directory sumber, dan tidak boleh ada modul sumber.

Beberapa tips untuk para ahli:
  * Kita dapat menggunakan `-O` atau `-OO` mengaktifkan perintah Python untuk mengurangi ukuran modul yang dikompilasi. Saklar `-O` menghapus pernyataan tegas assert, sedangkan saklar `-OO` menghapus pernyataan tegas assert dan string `__doc__`. Karena beberapa program bergantung pada ketersediaannya, Anda hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul `Optimized` memiliki tag `opt-` dan biasanya lebih kecil. Rilis di masa depan dapat mengubah efek pengoptimalan.
  * Suatu program tidak berjalan lebih cepat ketika itu dibaca dari file `.pyc` daripada ketika itu dibaca dari file `.py;` satu-satunya hal yang lebih cepat tentang berkas `.pyc` adalah kecepatan memuatnya.
  * Modul `compileall` dapat membuat berkas .pyc untuk semua modul dalam direktory.
  * Ada detail lebih lanjut tentang proses ini, termasuk bagan alur keputusan, di `PEP 3147`.

**6.2. Standard Modules / Modul Standar**

---

Python dilengkapi dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python. Beberapa modul dibangun ke dalam interpreter yang menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti pemanggilan sistem. 

Himpunan modul tersebut adalah opsi konfigurasi yang juga tergantung pada platform yang mendasarinya. Sebagai contoh, modul `winreg` hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: `sys`, yang dibangun ke dalam setiap interpreter Python. Variabel `sys.ps1` dan `sys.ps2` menentukan string yang digunakan sebagai prompt primer dan sekunder.

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua variabel tersebut hanya ditentukan jika interpreter dalam mode interaktif.

Variabel `sys.path` adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Hal tersebut diinisialisasi ke jalur default yang diambil dari variabel lingkungan `PYTHONPATH`, atau dari bawaan-bawaan lain jika `PYTHONPATH` tidak disetel. Kita dapat memondifikasinya menggunakan operasi standar untuk list:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

**6.3. The dir() Function / Fungsi dir()**

---

Fungsi bawaan `dir()` digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul. Dimana fungsi ini mengembalikan `list string` yang diurutkan:

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

Kemudian jika Tanpa argumen, `dir()` mencantumkan nama yang telah kita tentukan saat ini:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

Perhatikan bahwa fungsi ini mencantumkan semua jenis nama seperti (variabel, modul, fungsi, dan lain-lain). Fungsi dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika kita ingin mendaftarkan itu, maka fungsi harus didefinisikan dalam modul standar builtins:

```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

**6.4. Packages / Paket**

---

Paket adalah cara penataan namespace Python dengan menggunakan `dotted module names`. Sebagai contoh, nama modul `A.B` menetapkan submodule bernama `B` dalam sebuah paket bernama `A`. Sama seperti penggunaan modul mempermudah penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik untuk mempermudahkan penulis paket multi-modul seperti `NumPy` atau `Pillow` dari harus khawatir tentang nama modul masing-masing.

Misalkan ketika kita ingin merancang koleksi modul `(Paket)` untuk penanganan berkas suara dan data suara yang seragam. Ada banyak format berkas suara yang berbeda (biasanya dikenali oleh ekstensi mereka, misalnya `.wav, .aiff, .au`), jadi kita mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin kita lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, menciptakan efek stereo buatan), jadi selain itu kita akan menulis aliran modul tanpa henti untuk melakukan operasi ini. Berikut adalah struktur yang mungkin untuk paket kita (dinyatakan dalam hierarki sistem file):

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Saat kita mengimport sebuah paket, Python akan mencari melalui directory `sys.path` mencari subdirectory paket.

Berkas `__init__.py` diperlukan untuk membuat Python memperlakukan direktory yang berisi file sebagai paket. Hal ini mencegah direktory dengan nama umum, seperti string, menyembunyikan modul valid yang muncul kemudian pada jalur pencarian modul. Dalam kasus yang paling sederhana, `:file: __init__.py` dapat berupa file kosong, tetapi juga dapat menjalankan kode inisialisasi untuk paket atau mengatur variabel `__all__`.

Pengguna paket dapat mengimport modul individual dari paket, misalnya:

```python
import sound.effects.echo
```

hal tersebut memuat submodule `sound.effects.echo`. Hal tersebut harus dirujuk dengan nama lengkap yakni:

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Atau dengan cara alternatif mengimport submodul seperti:

```python
from sound.effects import echo
```

Hal di atas juga akan memuat submodul `:mod: echo` dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Namun juga ada variasi lain ketika mengimport fungsi atau variabel yang diinginkan secara langsung dengan:

```python
from sound.effects.echo import echofilter
```

Dan hasilnya akan sama memuat submodul echo, tetapi ini membuat fungsinya menjadi `echofilter()` langsung tersedia dan tidak lagi diikuti dengan `echo.`:

```python
echofilter(input, output, delay=0.7, atten=4)
```

Perhatikan bahwa ketika menggunakan `from package import item`, item tersebut dapat berupa submodul (subpaket) dari paket, atau beberapa nama lain yang ditentukan dalam paket, seperti fungsi, kelas atau variabel. Pernyataan `import` pertama menguji apakah item tersebut didefinisikan dalam paket. Jika tidak, maka ini akan dianggap sebagai modul dan mencoba membuatnya. Jika gagal menemukannya, pengecualian maka `ImportError` akan muncul.

Sebaliknya, ketika menggunakan sintaksis seperti `import item.subitem.subsubitem`, setiap item kecuali yang terakhir harus berupa paket. Item terakhir dapat berupa modul atau paket tetapi tidak bisa berupa kelas atau fungsi atau variabel yang didefinisikan dalam item sebelumnya.

**6.4.1. Importing * From a Package / Mengimpor * Dari Paket**

---

Sekarang apa yang terjadi ketika pengguna menulis `from sound.effects import *`? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke sistem file, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor submodul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika submodul diimport secara eksplisit.

Satu-satunya solusi adalah bagi pembuat paket untuk memberikan indeks paket secara eksplisit. Pernyataan import menggunakan konvensi berikut: 
  * jika suatu paket punya kode `__init __.py` yang mendefinisikan daftar bernama `__all__`, itu diambil sebagai daftar nama modul yang harus diimport ketika `from package import *` ditemukan. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. 
  * Atau  Pembuat paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat penggunaan untuk mengimport `*` dari paket mereka. Sebagai contoh, berkas `sound/effects/__init__.py` dapat berisi kode berikut:

```python
__all__ = ["echo", "surround", "reverse"]
```

Ini berarti bahwa `from sound.effects import *` akan mengimport tiga submodul bernama dari paket `sound`.

Jika `__all__` tidak didefinisikan, pernyataan `from sound.effects import *` tidak mengimport semua submodul dari paket `sound.effects` ke namespace saat ini; itu hanya memastikan bahwa paket `sound.effects` telah diimport (mungkin menjalankan kode inisialisasi apa pun di `__init__.py`) dan kemudian mengimport nama apa pun yang didefinisikan dalam paket. Ini termasuk semua nama yang didefinisikan (dan submodul yang dimuat secara eksplisit) oleh `__init__.py`. hal itu juga termasuk semua submodul dari paket yang secara eksplisit dimuat oleh sebelumnya pernyataan `import`. Pertimbangkan kode ini:

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

Dalam contoh ini, modul `echo` dan `surround` diimport dalam namespace saat ini karena mereka didefinisikan dalam paket `sound.effects` ketika paket `from...import` Pernyataan dieksekusi. (Ini juga berfungsi ketika `__all__` didefinisikan.)

Meskipun modul-modul tertentu dirancang hanya untuk mengekspor nama-nama yang mengikuti pola tertentu ketika Anda menggunakan import `*`, itu masih dianggap praktik buruk dalam lingkungan kode produksi production.

Ingat, tidak ada yang salah dengan menggunakan `from package import specific_submodule`. Sebenarnya, ini adalah notasi yang disarankan kecuali modul import perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.

**6.4.2. Intra-package References / Referensi Intra-paket**

---

Ketika paket disusun menjadi `subpaket` (seperti pada paket sound pada contoh), Kita dapat menggunakan `import absolut` untuk merujuk pada submodul dari `siblings packages`. Misalnya, jika modul `sound.filters.vocoder` perlu menggunakan modul `echo` dalam paket `sound.effects`, hal tersebut dapat menggunakan `from sound.effects import echo`.

Kita juga dapat menulis `import relatif`, dengan bentuk `from module import name` pada pernyataan import. Import ini menggunakan titik-titik di awalan untuk menunjukkan paket saat ini dan induk yang terlibat dalam `import relatif`. Dari modul `surround` misalnya, Anda dapat menggunakan:

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Perhatikan bahwa `import relatif` didasarkan pada nama modul saat ini. Karena nama modul utama selalu `__main__`, modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan `import absolut`.

**6.4.3. Packages in Multiple Directories / Paket di Beberapa Direktori**

---

Paket mendukung satu atribut khusus lagi, `__path__`. Hal ini diinisialisasi menjadi daftar yang berisi nama direktory yang menyimpan file paket: `__init__.py` sebelum kode dalam file tersebut dieksekusi. 

Variabel ini dapat dimodifikasi, hal itu memengaruhi pencarian `modul` dan `subpackage` di masa depan yang terkandung dalam paket.

Meskipun fitur ini tidak sering dibutuhkan, fitur ini dapat digunakan untuk memperluas rangkaian modul yang ditemukan dalam suatu paket.