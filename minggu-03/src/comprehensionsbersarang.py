#List Comprehensions Bersarang
#berikut matriks 3x4 yang di implementasikan sebagai daftar list 3 dari daftar list 4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#Pemahaman daftar list comprehension yang akan mengubah baris dan kolom:
[[row[i] for row in matrix] for i in range(4)]

#contoh di atas setara dengan:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

#dan juga sama dengan:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed

#fungsi bawaan untuk pernyataan aliran flow yang kompleks menggunakan fungsi zip()
list(zip(*matrix))