#memberikan tabel sebagai argumen kata kunci keyword argument dengan notasi '**'.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#output
'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'