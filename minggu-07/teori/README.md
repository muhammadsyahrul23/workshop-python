# BAB 9 
# Classes

Kelas-kelas (classes) merupakan sarana untuk menggabungkan data dan fungsionalitas bersama. Jika membuat kalas baru akan menghasilkan objek dengan tipe baru, yang memungkinkan dibuatnya instance baru dari tipe itu. Setiap instance dari kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya.  Dibandingkan dengan bahasa pemrograman lain, mekanisme klas python menambah kelas dengan minimum sintaksis.  Ini adalah campuran dari mekanisme kelas yang ditemukan dalam C++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat menimpa metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama .

## 9.1. A Word About Names and Objects (Sepatah Kata Tentang Nama dan Objek)
Objek memiliki kepribadian, dan banyak nama (dalam cakupan yang berbeda) dapat terikat pada objek yang sama. Ini disebut alias dalam bahasa lain. Alias memiliki efek yang berpotensi mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti list, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk tujuan prosedural, karena alias berperilaku seperti pointer dalam beberapa hal. Misalnya, melewatkan sebuah objek adalah murah karena implementasinya hanya melewati sebuah pointer; jika suatu fungsi memodifikasi objek yang dilewatkan sebagai parameter, pemanggil akan melihat perubahan - ini menghilangkan kebutuhan akan dua mekanisme yang berbeda untuk melewatkan argumen argument passing seperti dalam Pascal.

## 9.2. Python Scopes and Namespaces (Lingkup Python dan Namespaces)
Sebuah namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan. Contoh ruang nama namespace adalah: himpunan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian bawaan); nama-nama global dalam sebuah modul; dan nama-nama lokal dalam pemanggilan fungsi. Hal penting yang perlu diketahui tentang ruang nama namespace adalah sama sekali tidak ada hubungan antara nama dalam ruang nama namespace yang berbeda; misalnya, dua modul yang berbeda dapat mendefinisikan fungsi maximize tanpa kebingungan --- pengguna modul harus memberikan awalan dengan nama modul.

scope adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. "Directly accessible" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha menemukan nama tersebut di namespace. Meskipun cakupan scopes ditentukan secara statis, mereka digunakan secara dinamis. Setiap saat selama eksekusi, setidaknya ada 3 atau 4 cakupan bersarang yang ruang nama-nya namespaces dapat diakses secara langsung:
* ruang lingkup scope terdalam, yang dicari pertama kali, berisi nama-nama lokal
* lingkup scope dari setiap fungsi penutup, yang dicari dimulai dengan lingkup penutup terdekat, berisi nama-nama non-lokal, tetapi juga non-global
* lingkup berikutnya next-to-last berisi nama global modul saat ini
* ruang lingkup scope terluar (dicari terakhir) adalah namespace yang mengandung nama bawaan

Jika sebuah nama dideklarasikan sebagai global, semua referensi dan penugasan langsung masuk ke lingkup perantara yang berisi nama global modul. Untuk mengembalikan variabel yang ditemukan di luar cakupan terdalam, Anda dapat menggunakan pernyataan nonlocal; jika tidak dideklarasikan non-lokal, variabel tersebut hanya-baca (mencoba menulis ke variabel semacam itu hanya akan membuat lokal baru di variabel cakupan terdalam, membiarkan variabel eksternal dengan nama yang sama tidak berubah). Semua operasi yang memperkenalkan nama-nama baru menggunakan lingkup lokal: khususnya, pernyataan import dan definisi fungsi mengikat modul atau nama fungsi di lingkup lokal. Pernyataan global dapat digunakan untuk menunjukkan bahwa variabel tertentu hidup dalam lingkup global dan harus kembali ke sana; pernyataan nonlocal menunjukkan bahwa variabel tertentu hidup dalam cakupan terlampir dan harus dikembalikan ke sana.

### 9.2.1 Scopes and Namespaces Example
Dibawah ini merupakan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda, dan bagaimana global dan nonlocal memengaruhi pengikatan variabel:
```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
pada bagian pemberian nilai local (yang bawaan) tidak berubah "sope_tests" pengikatan spam. Dan pemberian nilai nonlocal mengubah "scope_test's" pengikatan spam, dan pemberian nilai global mengubah pengikatan level modul. Pada program di atas tidak ada pengikatan sebelumnya untuk spam sebelum pemberian nilai global.

## 9.3. A First Look at Classes (Pandangan Pertama tentang Kelas)
### 9.3.1 Class Definition Syntax (Sintaks Definisi Kelas)
dibawah ini bentuk definisi kelas paling sederhana:
```python
    <statement-1>
    .
    .
    .
    <statement-N>
```
Definisi kelas sama seperti peryataan def, harus dieksekusi sebelum mereka memiliki efek. kita dapat menempatkan definisi kelas di cabang dari peryataan if, atau di dalam suatu fungsi. Ketika definisi kelas dimasukkan, maka namespace baru dibuat, dan digunakan sebagai lingkup scope lokal --- dengan demikian, semua tugas untuk variabel lokal masuk ke namespace baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.
Ketika definisi kelas dipertahankan secara normal (sampai akhir), objek kelas dibuat. Ini pada dasarnya membungkus konten namespace yang dihasilkan oleh definisi kelas; Kita akan belajar lebih banyak tentang objek kelas di bagian selanjutnya. Lingkup  lokal awal (efektif segera sebelum memasuki definisi kelas) diaktifkan kembali dan objek kelas terikat di sini ke nama kelas yang diberikan dalam header definisi kelas (ClassName dalam contoh).

### 9.3.2. Class Objects(Objek Kelas)
 Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat. Jadi, jika definisi kelas tampak seperti dibawah ini:
 ```python
 class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
penjelasan:  MyClass.i dan MyClass.f adalah referensi atribut yang valid, masing-masing mengembalikan integer dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga Anda dapat mengubah nilai MyClass.i oleh penugasan. __doc__ juga merupakan atribut yang valid, mengembalikan docstring milik kelas: "A simple example class".

instantiation kelas menggunakan notasi fungsi. Hanya berpura-pura bahwa objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):
```python
x = MyClass()
```
membuat instance baru dari kelas dan menetapkan objek ini ke variabel lokal x.

Operasi instansiasi ("calling" objek kelas) membuat objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan kondisi awal tertentu. Oleh karena itu sebuah kelas dapat mendefinisikan metode khusus bernama __init__(), seperti dibawah ini:
```python
def __init__(self):
    self.data = []
```
Ketika sebuah kelas mendefinisikan metode __init__(), instantiasi kelas secara otomatis memanggil __init__() untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, contoh baru yang diinisialisasi dapat diperoleh oleh:
```python
x = MyClass()
```

### 9.3.3. Objek Instance
Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data, dan metode. data attributes sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan.
```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```
Ketika definisi kelas dipertahankan secara normal (sampai akhir), objek kelas dibuat. Ini pada dasarnya membungkus konten namespace yang dihasilkan oleh definisi kelas; Kita akan belajar lebih banyak tentang objek kelas di bagian selanjutnya. Lingkup  lokal awal (efektif segera sebelum memasuki definisi kelas) diaktifkan kembali dan objek kelas terikat di sini ke nama kelas yang diberikan dalam header definisi kelas (ClassName dalam contoh).Jenis lain dari referensi properti instance adalah metode. Metode adalah fungsi yang "milik" untuk suatu objek. (Dalam Python, istilah metode tidak unik untuk instance kelas: jenis objek lain juga dapat memiliki metode. Misalnya, objek daftar telah memanggil metode. tambah, sisipkan, hapus, urutkan, dll. Namun, dalam diskusi berikut, kami akan secara eksklusif menggunakan istilah metode  untuk menggambarkan metode objek instance kelas, kecuali disebutkan secara eksplisit.)

### 9.3.5. Class and Instance Variables (Variabel Kelas dan Instance)
Secara umum, variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance kelas:
```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
Seperti yang dibahas dalam Sepatah Kata Tentang Nama dan Objek, data bersama dapat memiliki efek yang mengejutkan dengan melibatkan objek mutable seperti daftar lists dan kamus dictionaries. Sebagai contoh, daftar tricks dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua Dog instance:
```python
lass Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```
Desain kelas yang benar harus menggunakan variabel instance sebagai gantinya:
class Dog:
```python
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
## 9.4. Random Remarks
Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance:
```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
Atribut data dapat dirujuk oleh metode dan juga oleh pengguna biasa ("clients") dari suatu objek. Faktanya, tidak ada dalam Python yang memungkinkan untuk menegakkan enforce data yang disembunyikan --- semuanya didasarkan pada konvensi. (Di sisi lain, implementasi Python, ditulis dalam C, dapat sepenuhnya menyembunyikan detail implementasi dan mengontrol akses ke objek jika perlu; ini dapat digunakan oleh ekstensi ke Python yang ditulis dalam C.). 

Objek fungsi apa pun yang merupakan atribut kelas menentukan metode untuk instance dari kelas itu. Tidak perlu bahwa definisi fungsi tertutup secara teks dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga ok. Sebagai contoh:
```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
Sekarang f, g dan h adalah semua atribut class C yang merujuk ke objek-objek fungsi, dan akibatnya semuanya adalah metode instance dari C --- h sama persis dengan g. Perhatikan bahwa praktik ini biasanya hanya membingungkan pembaca program.

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen self:
```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```
Metode dapat merujuk nama global dengan cara yang sama seperti fungsi biasa. Ruang lingkup scope global yang terkait dengan suatu metode adalah modul yang berisi definisinya. (Kelas tidak pernah digunakan sebagai ruang lingkup scope global.) Sementara seseorang jarang menemukan alasan yang baik untuk menggunakan data global dalam suatu metode, ada banyak penggunaan sah lingkup global: untuk satu hal, fungsi dan modul yang diimpor ke dalam lingkup global dapat digunakan oleh metode, serta fungsi dan kelas yang didefinisikan di dalamnya. Biasanya, kelas yang berisi metode itu sendiri didefinisikan dalam lingkup global ini, dan di bagian selanjutnya kita akan menemukan beberapa alasan bagus mengapa suatu metode ingin merujuk kelasnya sendiri.

Setiap nilai adalah objek, dan karenanya memiliki kelas (juga disebut sebagai type). Ini disimpan sebagai object.__class__.

## 9.5. Inheritance(Pewarisan)
Sintaks untuk definisi kelas turunan terlihat seperti ini:
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Mengeksekusi definisi kelas turunan memberikan hasil yang sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi properti: jika atribut yang diminta tidak ditemukan di kelas, pencarian akan dilanjutkan untuk menemukan kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari  kelas lain.   Tidak ada yang istimewa tentang turunan kelas turunan: DerivedClassName() membuat turunan baru dari kelas. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, menurunkan urutan kelas dasar jika perlu, dan referensi metode yang valid jika mengembalikan objek fungsi.

Python memiliki dua fungsi bawaan yang bekerja dengan warisan:

*Gunakan isinstance() untuk memeriksa jenis instance: isinstance(obj, int) akan menjadi True hanya jika obj.__class__ adalah int atau beberapa kelas yang diturunkan dari int.

*Gunakan issubclass() untuk memeriksa warisan kelas: issubclass(bool, int)``adalah ``True karena bool adalah subkelas dari int. Namun, issubclass(float, int) adalah False karena float bukan subkelas dari int.

### 9.5.1. Multiple Inheritance(Pewarisan Berganda)
Python mendukung bentuk pewarisan berganda juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti dibawah:
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Mengeksekusi definisi kelas turunan memberikan hasil yang sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi properti: jika atribut yang diminta tidak ditemukan di kelas, pencarian akan dilanjutkan untuk menemukan kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri diturunkan dari  kelas lain.   Tidak ada yang istimewa tentang turunan kelas turunan: DerivedClassName() membuat turunan baru dari kelas. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, menurunkan urutan kelas dasar jika perlu, dan referensi metode yang valid jika mengembalikan objek fungsi.Dalam kebanyakan kasus, dalam kasus paling sederhana Anda dapat memikirkan untuk mencari properti yang diwarisi dari superclass seperti depth-first, left-to-right, alih-alih mencari dua kali dalam kelas yang sama, terdapat tumpang tindih dalam hierarki. Jadi jika properti tidak ditemukan di DerivedClassName, maka akan dicari di Base1, kemudian (secara rekursif) di kelas dasar  Base1, dan jika tidak ditemukan di sana, akan dicari di Base2 dan seterusnya.  Sebenarnya, ini sedikit lebih rumit dari itu; urutan resolusi metode berubah secara dinamis untuk mendukung panggilan kooperatif ke super(). Pendekatan ini dikenal dalam beberapa bahasa warisan ganda sebagai metode panggilan berikutnya dan lebih kuat daripada panggilan super  dalam bahasa warisan tunggal. 
 Pengurutan otomatis diperlukan karena semua contoh pewarisan berganda menunjukkan satu atau lebih hubungan berlian (di mana setidaknya salah satu superclass dapat diakses melalui banyak jalur dari kelas bawah). Misalnya, semua kelas mewarisi dari objek, jadi setiap pewarisan berganda menyediakan lebih dari satu jalur ke: kelas: `objek`. Untuk mencegah mengakses kelas dasar  lebih dari sekali, algoritma linier dinamis mengatur urutan pencarian dengan cara  mempertahankan urutan kiri-ke-kanan yang ditentukan di setiap kelas, yang hanya memanggil setiap kelas induk satu kali dan bersifat monoton (mis. kelas dapat disubklasifikasikan tanpa mempengaruhi urutan prioritas semua orang). Secara bersama-sama, properti ini memungkinkan untuk merancang kelas yang andal dan dapat diperluas dengan banyak pewarisan.

## 9.6. Private Variables(Variabel Privat)
Variabel instance "Private" yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (mis. _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.
Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. Sebagai contoh:
```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
Contoh di atas akan berfungsi bahkan jika MappingSubclass akan memperkenalkan sebuah pengidentifikasi __update karena diganti dengan _Mapping__update di kelas Mapping dan _MappingSubclass__update di kelas MappingSubclass masing-masing.

Perhatikan bahwa aturan mangling sebagian besar dirancang untuk menghindari kecelakaan; masih dimungkinkan untuk mengakses atau memodifikasi variabel yang dianggap pribadi. Ini bahkan dapat berguna dalam keadaan khusus, seperti di debugger.

Perhatikan bahwa kode yang dilewatkan ke exec() atau eval() tidak menganggap nama kelas classname dari kelas yang dipanggil sebagai kelas saat ini; ini mirip dengan efek pernyataan global, yang efeknya juga terbatas pada kode yang dikompilasi-byte byte-compiled bersama. Pembatasan yang sama berlaku untuk getattr(), setattr() dan delattr(), serta saat mereferensikan __dict__ secara langsung.

## 9.7. Odds and Ends (Barang Sisa Odds and Ends)
Terkadang berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau "struktur" C yang mengelompokkan beberapa elemen data bernama bersama-sama. Definisi kelas kosong akan melakukannya:
```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
epotong kode Python yang mengharapkan tipe data abstrak tertentu sering dapat dilewatkan kelas yang mengemulasi metode tipe data itu sebagai gantinya. Misalnya, jika Anda memiliki fungsi yang memformat beberapa data dari objek file, Anda dapat mendefinisikan kelas dengan metode read() dan readline() yang mendapatkan data dari buffer string sebagai gantinya, dan meneruskan itu sebagai argumen.

Objek metode instance memiliki atribut, juga: m.__self__ adalah objek instan dengan metode m(), dan m.__func__ adalah objek fungsi yang sesuai dengan metode tersebut.

## 9.8. Iterators
Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek penampung container dapat dibuat perulangan menggunakan pernyataan for:
```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

Penggunaan iterator meliputi pervades dan menyatukan Python. Di belakang layar, pernyataan for memanggil iter() pada objek penampung container. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__() yang mengakses elemen dalam penampung container satu per satu. Ketika tidak ada lagi elemen, __next__() memunculkan pengecualian StopIteration yang memberi tahu perulangan for untuk mengakhiri. Anda dapat memanggil metode __next__() menggunakan next() fungsi bawaan; contoh ini menunjukkan cara kerjanya:
```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas Anda. Definisikan metode __iter__() yang mengembalikan objek dengan metode __next__(). Jika kelas mendefinisikan __next__(), maka __iter__() bisa langsung mengembalikan self
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
```

## 9.9. Generators(Pembangkit Generator)
Generators adalah sebuah tool yang sederhana dan simpel untuk membuat sebuah iterasi. Itu ditulis seperti fungsi biasa tapi menggunakan pernyataan yield setiap kali ingin mengembalikan sebuah data. Tiap kali next() itu dipanggil, generators tersebut akan melanjutkan di mana hal itu berhenti (itu akan mengingat semua nilai dan pernyataan mana yang terakhir dieksekusi). Sebuah contoh menunjukkan bahwa generator sangat mudah dibuat
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```
```python
>>> for char in reverse('golf'):
...     print(char)
...
```
Apa pun yang dapat dilakukan dengan pembangkit generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan pada bagian sebelumnya. Apa yang membuat pembangkit generator sangat kompak adalah bahwa metode __iter__() dan __next__() dibuat secara otomatis.

Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara pemanggilan. Ini membuat fungsi lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan menggunakan variabel instan seperti self.index dan self.data.

Selain pembuatan metode otomatis dan menyimpan status program, ketika pembangkit generator berhenti, mereka secara otomatis menimbulkan StopIteration. Secara kombinasi, fitur-fitur ini membuatnya mudah untuk membuat iterator tanpa lebih dari sekadar menulis fungsi biasa.

## 9.10. Generator Expressions(Ekspresi Pembangkit Generator)
Beberapa pembangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar list comprehensions setara.
Contoh:
```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
```
