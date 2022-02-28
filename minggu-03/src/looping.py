#Teknik Perulangan
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#indeks posisi dan nilai terkait dapat diambil pada saat yang sama menggunakan fungsi enumerate().
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#Untuk mengulang dua urutan atau lebih secara bersamaan, entri dapat dipasangkan dengan fungsi zip().
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil fungsi reversed().
for i in reversed(range(1, 10, 2)):
    print(i)

#Untuk mengulangi sebuah urutan sequence dalam susunan yang diurutkan
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#membuat daftar list baru
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data