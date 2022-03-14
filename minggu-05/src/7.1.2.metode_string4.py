#membuat string dengan melewatkan dict dan menggunakan tanda kurung siku '[]' untuk mengakses kunci dari dict
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
     'Dcab: {0[Dcab]:d}'.format(table))

#output
'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'