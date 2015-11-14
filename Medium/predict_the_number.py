data = ["0", "5", "101", "25684"]

def find_power(n):
	p = 0
	num = 2**p
	while True:
		p += 1
		num = 2**p
		if num > n:
			return p - 1
			break

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	num = int(test)
	iters = 0
	while num > 0:
		p = find_power(num)
		iters += 1
		num = num - 2**p
	if iters % 3 == 0:
		print 0
	elif iters % 3 == 1:
		print 1
	elif iters % 3 == 2:
		print 2	

#test_cases.close() 