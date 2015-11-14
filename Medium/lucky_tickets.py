data = ["4", "6", "8"]

from math import factorial

def n_choose_k(n, k):
	r = factorial(n) / (factorial(k) * factorial(n-k))
	return r

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	n = test.rstrip()
	dig_num = int(n)
	n = 9*dig_num // 20 + 1
	ticket_numbers = 0
	for i in range(0, n):
		x = (-1)**i * n_choose_k(dig_num, i) * n_choose_k(dig_num + (9*dig_num // 2) - 1 - 10*i, dig_num - 1)
		ticket_numbers += x
	print ticket_numbers

#test_cases.close()