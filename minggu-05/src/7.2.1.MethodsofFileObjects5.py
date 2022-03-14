f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
# 16 (Output)
f.seek(5)      # Pergi ke byte ke-6 dalam file
# 5 (Output)
f.read(1)
# b'5' (Output)
f.seek(-3, 2)  # Pergi ke byte ke-3 sebelum akhir
# 13 (Output)
f.read(1)
# b'd' (Output)