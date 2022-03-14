#membaca konten file dengan memaanggil f.read(size)
f.read()
f.read()

#string yang hanya berisi satu baris baru.
f.readline()

#membaca baris dari file
for line in f:
     print(line, end='')

#menulis konten string ke berkas
f.write('This is a test\n')

#objek byte (dalam mode biner) -- sebelum menulisnya:
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)

#mengubah posisi objek file, gunakan f.seek(offset, whence)
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)