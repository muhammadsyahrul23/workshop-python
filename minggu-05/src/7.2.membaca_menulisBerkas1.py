#menggunakan kata kunci with saat berurusan dengan objek file
with open('workfile') as f:
    read_data = f.read()
# We can check that the file has been automatically closed.
f.closed

#output
'True'