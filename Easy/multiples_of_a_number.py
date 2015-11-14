
import sys
test_cases = open(sys.argv[1], 'r')
data = test_cases.readlines()
for test in data:
	num = test.split(",")
	x = int(num[0])
	n = int(num[1])
	if n >= x:
		print n*2
	else:
		k = 2
		S = n
		while S < x:
			S = n*k
			k = k + 1
		print S