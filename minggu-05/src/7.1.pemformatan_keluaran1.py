#membuat dengan menggunakan metode str.format() dari string
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)

#output
' 42572654 YES votes  49.67%'