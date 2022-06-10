# Minggu 14
# Pengantar Machine Learning dengan scikit-learn

Di bagian ini, kami memperkenalkan kosakata pembelajaran mesin yang kami gunakan di seluruh scikit-learn dan memberikan contoh pembelajaran sederhana.

## Machine Learning: pengaturan masalah

Secara umum, masalah learning mempertimbangkan satu set n sampel data dan kemudian mencoba memprediksi sifat data yang tidak diketahui. Jika setiap sampel lebih dari satu angka dan, misalnya, entri multi-dimensi (alias  data multivariat), dikatakan memiliki beberapa atribut atau fitur.

Masalah learning terbagi dalam beberapa kategori:

- 	learning yang diawasi, di mana data dilengkapi dengan atribut tambahan yang ingin kita prediksi. Masalah ini dapat berupa:

    - klasifikasi: sampel termasuk dalam dua atau lebih kelas dan kami ingin belajar dari data yang sudah diberi label bagaimana memprediksi kelas data yang tidak berlabel. Contoh masalah klasifikasi adalah pengenalan digit tulisan tangan, di mana tujuannya adalah untuk menetapkan setiap vektor input ke salah satu dari jumlah kategori diskrit yang terbatas. Cara lain untuk berpikir tentang klasifikasi adalah sebagai bentuk pembelajaran yang diawasi secara diskrit (sebagai lawan dari kontinu) di mana seseorang memiliki jumlah kategori yang terbatas dan untuk masing-masing n sampel yang disediakan, salah satunya adalah dengan mencoba memberi label pada mereka dengan kategori atau kelas yang benar.

    - regresi: jika output yang diinginkan terdiri dari satu atau lebih variabel kontinu, maka tugas tersebut disebut regresi. Contoh masalah regresi adalah prediksi panjang salmon sebagai fungsi usia dan beratnya.

- learning tanpa pengawasan, di mana data pelatihan terdiri dari satu set vektor input x tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut mungkin untuk menemukan kelompok contoh serupa dalam data, di mana itu disebut pengelompokan, atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai estimasi kepadatan, atau untuk memproyeksikan data dari ruang dimensi tinggi ke dua atau tiga dimensi untuk tujuan visualisasi.

### Set pelatihan dan set pengujian

Machine Learning adalah tentang mempelajari beberapa properti dari kumpulan data dan kemudian menguji properti tersebut terhadap kumpulan data lain. Praktik umum dalam pembelajaran mesin adalah mengevaluasi algoritma dengan membagi kumpulan data menjadi dua. Yaitu sebagai set pelatihan, di mana kita mempelajari beberapa properti; dan yang lain mengatur set pengujian, di mana kita menguji properti yang dipelajari.

## Memuat contoh Dataset

scikit-learn hadir dengan beberapa himpunan data standar, misalnya  himpunan data iris dan digit untuk klasifikasi dan dataset diabetes untuk regresi.

Berikut ini, kita memulai interpreter Python dari shell kita dan kemudian memuat himpunan data iris dan digit. Konvensi notasi kami adalah bahwa $ menunjukkan shell prompt sementara >>> menunjukkan prompt interpreter Python:

```
$ python
```

```py
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```
Dataset adalah objek seperti kamus yang menyimpan semua data dan beberapa metadata tentang data. Data ini disimpan di anggota .data, yang merupakan  array n_samples, n_features. Dalam kasus masalah yang diawasi, satu atau lebih variabel respons disimpan di  anggota .target. Detail lebih lanjut tentang himpunan data yang berbeda dapat ditemukan di bagian khusus.

Misalnya, dalam kasus himpunan data digit, digits.data memberikan akses ke fitur yang dapat digunakan untuk mengklasifikasikan sampel digit:

```py
>>> print(digits.data)
[[ 0.   0.   5. ...   0.   0.   0.]
 [ 0.   0.   0. ...  10.   0.   0.]
 [ 0.   0.   0. ...  16.   9.   0.]
 ...
 [ 0.   0.   1. ...   6.   0.   0.]
 [ 0.   0.   2. ...  12.   0.   0.]
 [ 0.   0.  10. ...  12.   1.   0.]]
 ```

 dan digits.target memberikan kebenaran dasar untuk himpunan data digit, yaitu angka yang sesuai dengan setiap gambar digit yang kita coba pelajari:

```py
>>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
```

 ### Bentuk array data

 Data selalu berupa array 2D, bentuk (n_samples, n_features), meskipun data aslinya mungkin memiliki bentuk yang berbeda. Dalam kasus digit, setiap sampel asli adalah gambar bentuk (8, 8) dan dapat diakses menggunakan:

 ```py
 >>> digits.images[0]
array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
       [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
       [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
       [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
       [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
       [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
       [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
       [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])
```

Contoh sederhana pada himpunan data ini menggambarkan bagaimana mulai dari masalah asli seseorang dapat membentuk data untuk dikonsumsi dalam scikit-learn.

## Learning and predicting

Dalam kasus dataset digit, tugasnya adalah memprediksi, diberi gambar, digit mana yang diwakilinya. Kami diberi sampel dari masing-masing dari 10 kelas yang mungkin (digit nol hingga sembilan) di mana cocok dengan penaksir untuk dapat memprediksi kelas tempat sampel yang tidak terlihat berada.

Dalam scikit-learn, penaksir untuk klasifikasi adalah objek Python yang mengimplementasikan metode fit(X, y) dan predict(T).

Contoh penaksir adalah kelas sklearn.svm.SVC, yang mengimplementasikan klasifikasi vektor dukungan. Konstruktor penaksir mengambil sebagai argumen parameter model.

Untuk saat ini, kita akan mempertimbangkan penaksir sebagai black box:

```py
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
``` 

### Memilih parameter model

Dalam contoh ini, kita menetapkan nilai gamma secara manual. Untuk menemukan nilai yang baik untuk parameter ini, kita dapat menggunakan alat seperti grid search dan cross validation.

Instans penaksir clf (untuk pengklasifikasi) pertama kali dipasang ke model; yaitu, ia harus belajar dari model. Ini dilakukan dengan meneruskan set pelatihan ke  metode fit. Untuk set pelatihan, kita akan menggunakan semua gambar dari himpunan data, kecuali untuk gambar terakhir, yang akan kita simpan untuk prediksi. Kita memilih set pelatihan dengan  sintaks Python [:-1], yang menghasilkan array baru yang berisi semua kecuali item terakhir dari digits.data:

```py
>>>clf.fit(digits.data[:-1], digits.target[:-1])
SVC(C=100.0, gamma=0.001)
```

Sekarang kita dapat memprediksi nilai-nilai baru. Dalam hal ini, kita akan memprediksi menggunakan gambar terakhir dari digits.data. Dengan memprediksi, kita akan menentukan gambar dari set pelatihan yang paling cocok dengan gambar terakhir.

```py
>>>clf.predict(digits.data[-1:])
array([8])
```

## Conventions

penaksir scikit-learn mengikuti aturan tertentu untuk membuat perilaku mereka lebih prediktif. Ini dijelaskan secara lebih rinci dalam [Glosarium Istilah Umum dan Elemen API](https://scikit-learn.org/stable/glossary.html#glossary).

### type casting

Kecuali ditentukan, input akan dilemparkan ke float64:

```py
>>> import numpy as np
>>> from sklearn import kernel_approximation

>>> rng = np.random.RandomState(0)
>>> X = rng.rand(10, 2000)
>>> X = np.array(X, dtype='float32')
>>> X.dtype
dtype('float32')

>>> transformer = kernel_approximation.RBFSampler()
>>> X_new = transformer.fit_transform(X)
>>> X_new.dtype
dtype('float64')
```

Dalam contoh ini, X adalah float32, yang dilemparkan ke float64 oleh fit_transform(X).

Target regresi dilemparkan ke float64 dan target klasifikasi dipertahankan:

```py
>>> from sklearn import datasets
>>> from sklearn.svm import SVC
>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
SVC()

>>> list(clf.predict(iris.data[:3]))
[0, 0, 0]

>>> clf.fit(iris.data, iris.target_names[iris.target])
SVC()

>>> list(clf.predict(iris.data[:3]))
['setosa', 'setosa', 'setosa']
```

Di sini, predict() pertama  mengembalikan array bilangan bulat, karena iris.target (array bilangan bulat) digunakan dalam fit. Predict() kedua  mengembalikan array string, karena iris.target_names adalah untuk pemasangan.

### Refitting and updating parameters

Hyper-parameter dari penaksir dapat diperbarui setelah dibangun melalui metode set_params(). Memanggil fit() lebih dari sekali akan menimpa apa yang dipelajari oleh fit()sebelumnya:

```py
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC
>>> X, y = load_iris(return_X_y=True)

>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X, y)
SVC(kernel='linear')
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])

>>> clf.set_params(kernel='rbf').fit(X, y)
SVC()
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
```

Di sini, kernel default rbf pertama kali diubah menjadi linier melalui SVC.set_params() setelah penaksir dibangun, dan diubah kembali menjadi rbf untuk memperbaiki penaksir dan membuat prediksi kedua.

### Multiclass vs. multilabel fitting

Saat menggunakan  pengklasifikasi multikelas, tugas learning dan predict yang dilakukan tergantung pada format data target yang sesuai dengan:

```py
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```

Dalam kasus di atas, pengklasifikasi cocok pada array 1d label multiclass dan oleh karena itu metode predict() menyediakan prediksi multiclass yang sesuai. Dimungkinkan juga untuk menyesuaikan diri dengan array 2d indikator label biner:

```py
>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```

Di sini, pengklasifikasi adalah fit() pada representasi label biner 2d y, menggunakan LabelBinarizer. Dalam hal ini predict() mengembalikan array 2d yang mewakili prediksi multilabel yang sesuai.

Perhatikan bahwa contoh keempat dan kelima mengembalikan semua nol, menunjukkan bahwa mereka tidak cocok dengan tidak satu pun dari tiga label yang cocok. Dengan output multilabel, contoh juga dapat diberi beberapa label:

```py
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```

Dalam hal ini, pengklasifikasi sesuai dengan instans yang masing-masing diberi beberapa label. MultiLabelBinarizer digunakan untuk mengikat array 2d multilabel agar sesuai. Akibatnya, predict() mengembalikan array 2d dengan beberapa label yang diprediksi untuk setiap instance.