num = 9876

rev_n = 0

while num > 0:
  digit = num %10
  rev_n = rev_n *10 +digit
  num  = num // 10
print(rev_n)