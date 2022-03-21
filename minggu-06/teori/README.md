# BAB 8 
# Error and Exeptions

Sampai sekarang pesan kesalahan masih belum lebih dari yang disebutkan, tetapi jika kita telah mencoba contohnya, kita mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan yaitu: syntax errors dan exceptions.

---

## 8.1. Kesalahan Sintaksis (Syntax Errors)

Kesalahan sintaksis, juga dapat dikenal dengan kesalahan penguraian parsing, mungkin merupakan jenis keluhan paling umum yang akan kita dapatkan saat masih belajar Python:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

Pengurai parser mengulangi baris yang menyinggung dan menampilkan sedikit 'arrow' yang menunjuk pada titik paling awal di baris di mana kesalahan terdeteksi. Kesalahan disebabkan oleh token preceding panah: contohnya kesalahan terdeteksi pada fungsi `print()`, karena titik dua (`':'`)) hilang sebelum itu. Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari kalau-kalau masukan berasal dari skrip.

## 8.2. Pengecualian (Exeptions)

jika suatu pernyataan atau ungkapan secara sintaksis benar, hal tersebut dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut exceptions dan tidak fatal tanpa syarat: kita akan belajar cara menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, seperti contoh d bawah ini:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian ada berbagai jenis yang berbeda, dan tipe dicetak sebagai bagian dari pesan: tipe dalam contoh adalah `ZeroDivisionError`, `NameError` dan `TypeError`. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Hal ini berlaku untuk semua pengecualian bawaan, tetapi tidak harus sama untuk pengecualian yang dibuat pengguna. Nama pengecualian standar adalah pengidentifikasi bawaan (bukan kata kunci yang dipesan reserved keyword).

Sisa baris menyediakan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya. Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana pengecualian terjadi, dalam bentuk pelacakan balik tumpukan. Secara umum ini berisi baris sumber daftar traceback stack; namun, itu tidak akan menampilkan baris yang dibaca dari input standar. `Built-in Exceptions` memberikan daftar pengecualian bawaan dan artinya.

## 8.3. Menangani Pengecualian (Handling Exeptions)

Untuk menulis program yang menangani pengecualian yang dipilih. Perhatikan contoh berikut, yang meminta masukan dari pengguna sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menghentikan program (menggunakan Control-C atau apa pun yang didukung sistem operasi); perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan munculnya pengecualian `KeyboardInterrupt`.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pernyataan `try` berfungsi sebagai berikut.

  * Pertama, try clause (pernyataan(-pernyataan) di antara kata kunci `try` dan `except`) dieksekusi.
  * Jika tidak ada pengecualian terjadi, except clause dilewati dan eksekusi pernyataan :keyword: `try` selesai.
  * Jika pengecualian terjadi selama eksekusi klausa `try`, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci `kecuali`, klausa kecuali dijalankan, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali.
  * Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, hal tersebut diteruskan ke pernyataan percobaan luar; jika tidak ada penangan yang ditemukan, hal itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan `try` mungkin memiliki lebih dari satu klausa `kecuali`, untuk menentukan penanganan untuk pengecualian yang berbeda. Satu handler akan dieksekusi. Handler hanya menangani pengecualian yang terjadi di klausa try yang sesuai, bukan di handler lain dari pernyataan try yang sama. Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tupel dalam kurung, misalnya:

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

Kelas dalam klausa `kecuali/except` kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar daripadanya (tetapi tidak sebaliknya --- klausa kecuali yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Perhatikan bahwa jika klausa kecuali dibalik (dengan kecuali B terlebih dahulu), hal tersebut akan mencetak B, B, B --- pencocokan pertama klausa kecuali dapat dipicu.

Semua pengecualian mewarisinya dari `BaseException`, yang dapat digunakan  sebagai wildcard. Penggunaan ini sangat hati-hati, karena mudah untuk menutupi kesalahan program yang sebenarnya dengan cara ini! hal ini juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali pengecualian (memungkinkan penelepon untuk menangani pengecualian juga):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Sebagai alternatif, klausa pengecualian terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari `sys.exc_info()[1]`.

Pernyataan `try ... kecuali/except` memiliki klausa `else` opsional, yang jika ada, harus mengikuti semua klausa `kecuali/except`. Berguna untuk kode yang harus dijalankan jika klausa try tidak memunculkan eksepsi. Sebagai contoh:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan klausa else lebih baik daripada menambahkan kode tambahan ke klausa `try` karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan `try` ... :`keyword`: `!`except`.

Ketika pengecualian terjadi, hal tersebut memiliki nilai terkait, yang dikenal sebagai `argument` pengecualian. Kehadiran dan jenis argumen tergantung pada jenis pengecualian.

Klausa kecuali dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke instance pengecualian dengan argumen dapat disimpan di `instance.args`. Untuk kenyamanan, instance pengecualian mendefinisikan `__str__()` sehingga argumen dapat dicetak secara langsung tanpa harus merujuk ke `.args.` kita juga dapat membuat instance pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Jika pengecualian memiliki argumen, mereka dicetak sebagai bagian terakhir `('detail')` dari pesan untuk pengecualian yang tidak ditangani.

Pengendali pengecualian tidak hanya menangani pengecualian jika terjadi segera di klausa `try`, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam klausa try. Sebagai contoh:

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Memunculkan Pengecualian (Raising Exceptions)

Pernyataan `raise` memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi. Contohnya:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu-satunya argumen untuk `raise` menunjukkan pengecualian yang dimunculkan. Ini harus berupa `instance` pengecualian atau kelas pengecualian (kelas yang berasal dari `Exception`). Jika kelas pengecualian dikirimkan, itu akan secara implisit diinstansiasi dengan memanggil pembangunnya `constructor` tanpa argumen:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Jika kita perlu menentukan apakah pengecualian muncul tetapi tidak bermaksud menanganinya, bentuk yang lebih sederhana dari pernyataan raise memungkinkan kita untuk memunculkan kembali pengecualian:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5. Rantai Pengecualian (Exception Chaining)

Pernyataan `kenaikan/raise` memungkinkan opsional yang memungkinkan pengecualian rantai. Sebagai contoh:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

Hal ini dapat berguna saat kita mengubah pengecualian. Sebagai contoh:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam bagian `kecuali/except` atau `akhirnya/finally`. Ini dapat dinonaktifkan dengan menggunakan `dari None` idiom:

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

## 8.6. Pengecualian yang Ditentukan Pengguna (User-defined Exceptions)

Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru. Pengecualian biasanya berasal dari kelas `Exception`, baik secara langsung atau tidak langsung.

Kelas `pengecualian` dapat didefinisikan dengan apa pun yang dapat dilakukan oleh kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penanganan untuk `pengecualian`.

Sebagian besar pengecualian didefinisikan dengan nama yang diakhiri dengan `"Error"`, mirip dengan penamaan pengecualian standar.

## 8.7. Mendefinisikan Tindakan Pembersihan (Defining Clean-up Actions)

Pernyataan `try` memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan. Contohnya:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Jika ada klausa `finally`, klausa untuk finally akan dijalankan sebagai tugas terakhir sebelum pernyataan untuk `try` selesai. Klausa untuk `finally` dapat berjalan baik atau tidak apabila pernyataan try menghasilkan suatu pengecualian. Poin-poin berikut membahas kasus yang lebih kompleks saat pengecualian terjadi:
   * Jika pengecualian terjadi selama eksekusi klausa untuk :keyword: `!try`, maka pengecualian tersebut dapat ditangani oleh klausa `except`. Jika pengecualian tidak ditangani oleh klausa :keyword: `!except`, maka pengecualian dimunculkan kembali setelah klausa `finally` dieksekusi.
   * Pengecualian dapat terjadi selama pelaksanaan klausa `except` atau `else`. Sekali lagi, pengecualian akan muncul kembali setelah klausa `finally` telah dieksekusi.
   * Jika klausa terakhir mengeksekusi pernyataan `break`, `continue`, atau `return`, eksepsi tidak dimunculkan kembali.
   * Jika pernyataan klausa untuk try mencapai klausa `break`, `continue` atau :keyword:` return` maka, pernyataan untuk klausa finally akan dieksekusi sebelum break, continue atau return dieksekusi.
   * Jika klausa untuk :keyword:`!finally` telah menyertakan pernyataan `return`, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk finally dan dari klausa return, bukan nilai dari `try` pernayataan untuk return.

Contohnya:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

Contoh yang lebih rumit:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang kita lihat, klausa `finally` dieksekusi dalam peristiwa apa pun. `TypeError` yang ditimbulkan dengan membagi dua string tidak ditangani oleh klausa `except` dan karenanya kembali muncul setelah klausa `finally` telah dieksekusi.

Klausa `finally` berguna untuk melepaskan sumber daya `eksternal` (seperti berkas atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya tersebut berhasil.

## 8.8. Tindakan Pembersihan yang Sudah Ditentukan (Predefined Clean-up Actions)

Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka berkas dan mencetak isinya ke layar.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Masalah dengan kode ini adalah bahwa ia membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan `with` memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dieksekusi, `file f `selalu ditutup, bahkan jika ada masalah saat pemrosesan baris-baris. Objek yang, seperti berkas-berkas, memberikan tindakan pembersihan yang telah ditentukan, akan menunjukkan dalam dokumentasinya.