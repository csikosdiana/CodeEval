data = ["2", "16", "52", "3702"]

import string
N = list(string.ascii_uppercase)

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	num = int(test)
	names = ""
	if num <= 26:
		names = N[num-1]
	elif num <= 26**2:
		t = num // 26
		e = num % 26
		if e == 0:
			t = t - 1
			e = 26
		names = N[t-1] + N[e-1]
	elif num <= 26**3:
		sz = num // 26**2
		m = num - sz*26**2
		t = m // 26
		m = m - t*26
		e = m % 26
		if t == 0:
			sz = sz - 1
			t = 26
		if e == 0:
			t = t - 1
			e = 26
		names = N[sz-1] + N[t-1] + N[e-1]
	print names

#test_cases.close()