
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, (n/2)+1):
		if n%i == 0:
			return False
	return True

import sys
test_cases = open(sys.argv[1], 'r')
data = test_cases.readlines()
for test in data:
	num = test.split(",")
	x = int(num[0])
	y = int(num[1])
	Count = 0
	for i in range(x, y+1):
		p = is_prime(i)
		if p:
			Count = Count + 1
	print Count