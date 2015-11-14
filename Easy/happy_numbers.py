data = ['1', '7', '22']

def happy_numbers(n):
	D = dict()
	n = int(n)
	while n != 1:
		n = str(n)
		n = list(n)
		n = map(int, n)
		n2 = [i**2 for i in n]
		n = sum(n2)
		if n in D:
			return 0
		else:
			D[n] = 1
		
	
	return 1

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	H = happy_numbers(test)
	print H

#test_cases.close()