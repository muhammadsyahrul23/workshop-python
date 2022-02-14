# Tutorial Python

Python merupakan bahasa pemrograman yang berdaya dan mudah dipelajari. Python memiliki struktur data tingkat tinggi yang efisien dan pendekatan yang sederhana namun efektif untuk pemrograman berorientasi objek. Sintaksis Python yang elegan dan tipe dinamis, bersama dengan sifatnya yang diinterpretasikan, menjadikannya bahasa yang ideal untuk skrip dan pengembangan aplikasi yang cepat di banyak area di sebagian besar platform.

Interpreter Python dan pustaka standar yang luas tersedia secara bebas dalam bentuk kode sumber atau biner untuk semua platform utama dari situs Web Python. Interpreter Python mudah dikembangkan dengan fungsi dan tipe data baru diimplementasikan dalam C atau C++ (atau bahasa lain yang bisa dipanggil dari C) Python juga cocok sebagai bahasa tambahan untuk aplikasi yang dapat disesuaikan.

# Bab 1
---
Jika kita merupakan seorang pengembang sofware profesional, kita mungkin harus bekerja dengan beberapa pustaka atau bahasa pemograman seperti C/C++/Java tetapi ketika kita memakai bahasa pemograman ini memungkinkan menemukan siklus penulisan, kompilasi, pengujian, dan kompilasi ulang yang terlalu lambat. Itu akan membuat pekerjaan kita menjadi membosankan karena terlalu lama dalam penulisan code, kompilasi dan juga pengujiannya.

Dalam hal ini, Python menjadi solusi yang tepat
Kenapa? Sebagai contoh kasus ketika menulis program C/C++/Java memungkinkan untuk membutuhkan banyak waktu pengembangan untuk mendapatkan program draft pertama. Tetapi Python lebih mudah digunakan, serta tersedia di sistem operasi Windows, Mac OS X, dan Unix. Kemudian penggunaan Python dalam menyelesaikan pekerjaan dengan lebih cepat.

Python adalah bahasa yang ditafsirkan, yang dapat menghemat waktu kita selama pengembangan program karena tidak diperlukan kompilasi dan penautan. Interpreter dapat digunakan secara interaktif, yang membuatnya mudah bereksperimen dengan fitur-fitur bahasa, untuk menulis throw-away programs, atau untuk menguji fungsi selama pengembangan program bottom-up.

Python memungkinkan program ditulis secara ringkas dan mudah dibaca. Program yang ditulis dengan Python biasanya jauh lebih pendek daripada program C, C++, atau Java yang setara, karena beberapa alasan:
   * Tipe data tingkat tinggi memungkinkan Kita untuk mengekspresikan operasi yang kompleks dalam satu pernyatann;
   * Pengelompokan pernyataan dilakukan dengan indentasi alih-alih tanda kurung kurawal di awal dan akhir;

   * Tidak ada deklarasi variabel atau argumen yang diperlukan.

Python bersifat extensible yang artinya Python dapat dikembangkan untuk berbagai macam tugas, misalnya pembuatan aplikasi web atau pun desktop, proses analisis data, dll. Selain itu, Python juga terintegrasi dengan baik dengan berbagai macam bahasa pemrograman lainnya dan layanan enterprise. Di bagian bagian yang mulai melibatkan sumber daya komputasi yang cukup besar, kita dapat menggunakan fungsi yang ada di bahasa pemrograman lain yang bersifat low-level programming language (bahasa pemrograman yang sulit untuk dibaca dan ditulis oleh manusia) namun dikemas menjadi fungsionalitas yang ada di Python.

# Bab 2
---
**Menggunakan Interpreter Python**

Interpreter Python biasanya diinstall pada directory dalam komputer yakni pada `usr/local/bin/python3.10` Untuk mengakses atau memanggil Interpreter pada Unix/Linux dengan masuk dalam directory `usr/local/bin` setelah itu ketikan python.10 (sesuai dengan versi python yang diinstall). Kemudian untuk Windows versi Python dapat diinstall lewat platform Microsoft Store atau dapat menginstall py.exe launcher dan menggunakan command `py`

Interpreter beroperasi mirip dengan shell pada Unix/Linux, ketika dipanggil dengan masukan bawaan yang terhubung dengan perangkat tty. tty merupakan perintah Unix yang mencetak nama berkas yang terhubung ke input standar melalui output standar. Nama aplikasi ini berasal dari kata teletypewriter, yang disingkat menjadi "TTY", Interpreter membaca dan mengeksekusi perintah secara interaktif ketika dipanggil dengan argumen nama berkas.

Beberapa modul Python juga berguna sebagai skrip. Ini dapat dipanggil menggunakan `python -m module [arg] ...`, yang mengeksekusi berkas sumber untuk module seolah-olah kita telah menuliskan nama lengkap pada baris perintah. Ketika berkas digunakan, terkadang berguna untuk dapat menjalankan skrip dan masuk ke mode interaktif sesudahnya. Ini dapat dilakukan dengan menuliskan -i sebelum skrip.

Ketika diketahui oleh interpreter, nama skrip dan argumen tambahan sesudahnya diubah menjadi daftar string dan diberikan nilai variabel `argv` dalam modul `sys`. Kita dapat mengakses daftar ini dengan menjalankan `import sys`. Ketika nama skrip diberikan `-` (yang artinya standar masukan) sebagai contoh ketika command -c digunakan, maka `sys.argv[0]` diatur ke `-c`. Kemudian ketika `*module* : option: -m` digunakan, `sys.argv[0]` diatur ke nama lengkap modul yang digunakan. Opsi akan ditemukan setelah command `-c` atau module `-m` tidak dikonsumsi oleh pemrosesan opsi interpreter Python tetapi ditinggalkan di `sys.argv` untuk perintah atau modul yang akan ditangani.

Ketika perintah dibaca dari tty, interpreter dikatakan dalam ***interactive*** mode. Dalam mode ini interpreter dalam python disebut dengan ***primary prompt*** yakni tanda `>>>`. Kemudian ada juga yang disebut ***secondary prompt*** yakni `...` yang sering digunakan dipendeklarasian statment pada seleksi dan perulangan.

Kemudian untuk lingkungan Python secara bawaan menggunakan penulisan ***encoded** dalam `UTF-8`. Encode adalah proses penempatan urutan karakter (huruf, angka, tanda baca, dan symbol tertentu) ke dalam format khusus sehingga menjadi sebuah sandi. 

Dalam python mendeklarasikan penyandian ***encoding*** selain bawaan, baris komentar khusus harus ditambahkan sebagai baris pertama dalam berkas/file. dengan syntax `# -*- coding: encoding -*-` misalnya dalam pendeklarasian encoding pada ***Windows-1252*** yakni dengan syntax `-*- coding: cp1252 -*-`. Pengecualian untuk aturan baris pertama ketika kode sumber dimulai dengan UNIX "shebang" line. Shebang adalah urutan karakter yang terdiri dari tanda nomor karakter dan tanda seru di awal skrip. Ini juga disebut sha-bang, hashbang, pound-bang, atau hash-pling. Jadi, deklarasi `encoding` harus ditambahkan pada baris kedua setelah deklarasi UNIX "shebang" line.

# Bab 3
---
**Pengantar Informal Tentang Python**

Dalam Python, untuk pembuatan skrip atau source code terminal prompt yakni ditandai `>>>` yang disebut juga dengan ***primary prompt***. Ketika mengetikan skrip harus diperhatikan untuk diketikan setelah tanda `>>>` dan kemudian untuk baris yang tidak memiliki tanda `>>>` merupakan output dari interpreter.

Kemudian ada contoh lagi seperti penulisan komentar. Komentar dalam python dimulai dengan ***hash*** atau `#`. Sebuah komentar dapat muncul di awal baris atau dideklarasikan setelah code dibuat namun tidak dapat dideklarasikan pada string literal karena karakter hash dalam string literal hanyalah karakter hash dan menjadikan nilai dari string literal tersebut. Dimana hal ini bukan sifat dari komentar dalam source code yang berfungsi untuk mengklarifikasi kode dan tidak ditafsirkan pada Python.

Kemudian pada prompt Python kita juga bisa menggunakannya layaknya kalkulator. Interpreter bertindak sebagai kalkulator sederhana seperti kita dapat mengetikkan ekspresi padanya dan itu akan menulis nilainya. Sintaksis mudah ekspresi seperti operator `+`, `-`, `*`, dan `/` berfungsi seperti sebagian besar bahasa lain (misalnya pascal atau C), kemudian tanda kurung `()` dapat digunakan untuk pengelompokkan value/nilai.

Kemudian dalam pendeklarasian nilai/angka seperti bilangan bulat masuk dalam tipe `int`, untuk bilangan pecahan memiliki `float`. Kemudian terdapat juga division `/` selalu mengembalikan nilai float atau bilangan pecahan, untuk operator `//` dalam Python digunakan untuk menghitung floor division, dan kemudian untuk menhitung modulus menggunakan operator `%`. Dalam python juga memungkinkan mengunakan operator `**` untuk penghitungan pemangkatan.

Setiap pendeklarasian variabel harus diberikan sebuah value atau nilai dengan menggunakan tanda `=` karena jika tidak maka akan menimbulkan kesalahan. Dalam Python juga memiliki dukungan penuh untuk floating point. Dalam mode interaktif, ekspresi cetak terakhir diberikan ke variabel `_`. dimana variabel `_` akan menampung hasil dari pengerjaan sebelumnya. Selain `int` dan `float`, Python juga mendukung tipe angka lainnya seperti `Decimal` dan `Fraction` serta juga memiliki bawaan complex numbers dan menggunakan bahasa imajiner seperti penggunaan `j` atau `J` (contoh 3+5j)

Selain angka, Python juga dapat memanipulasi string atau teks, yang dapat diekspresikan dalam beberapa cara. dimana dapat dideklarasikan dengan menggunakan single quote `(' ')` atau menggunakan double quote `(" ")` serta tanda `\` digunakan untuk keluar dari kutipan. String disertakan dalam tanda kutip ganda jika string berisi kutipan tunggal dan tidak ada tanda kutip ganda, jika tidak maka akan dilampirkan dalam tanda kutip tunggal. Fungsi `print()` menghasilkan keluaran yang lebih mudah dibaca, dengan menghilangkan tanda kutip terlampir dan dengan mencetak karakter yang dipisahkan dan spesial.

Kemudian Jika Kita tidak ingin karakter yang diawali dengan `\` ditafsirkan sebagai karakter khusus, Anda dapat menggunakan raw strings dengan menambahkan r sebelum kutipan pertama. String literal dapat melebar hingga beberapa baris. Salah satu caranya adalah dengan menggunakan tanda kutip tiga: `"""..."""` atau `'''...'''`. Akhir baris secara otomatis termasuk dalam string, tetapi dimungkinkan untuk mencegahnya dengan menambahkan `\` di akhir baris. Selain itu juga dalam pendeklarasian string dapat digabungkan dengan penggunaan tanda `+` dan pengulangan kalimat menggunakan tanda `*`. Dua atau lebih string literals (yaitu yang terlampir di antara tanda kutip) di sebelah satu sama lain secara otomatis digabungkan.

String juga dapat diindeks atau indexed (disandikan), dengan karakter pertama memiliki indeks 0. Tidak ada tipe karakter yang terpisah; sebuah karakter hanyalah sebuah string berukuran satu. elain pengindeksan, slicing atau mengiris juga didukung. Sementara pengindeksan digunakan untuk mendapatkan karakter individual, slicing memungkinkan Kita untuk mendapatkan substring.

Python juga dapat mengetahui sejumlah tipe data compound atau gabungan, yang digunakan untuk pengelompokan nilai-nilainya. Yang paling serbaguna adalah list, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (items) antara tanda kurung siku `[]`. List atau daftar mungkin berisi items dari tipe yang berbeda, tetapi biasanya semua items memiliki tipe yang sama. Seperti string (dan semua bawaan lainnya tipe sequence), list atau daftar tersebut dapat diindekskan dan diiriskan. Semua operasi iris mengembalikan list atau daftar baru yang berisi elemen yang diminta. Ini berarti bahwa irisan berikut mengembalikan shallow copy dari list.

Tidak seperti string, yang immutable, list adalah mutable. Mutable adalah tipe data yang nilainya dapat diubah. Dalam pendeklarasian list kita dapat menambahkan item baru dengan menggunakan method `append()` dan penggunaan method `len()` untuk menghitung panjang/length dalam list.