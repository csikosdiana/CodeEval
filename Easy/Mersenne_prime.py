data = ['4', '308']

primes = [2, 3, 5, 7, 11, 13]

Mersenne_primes = []
for p in primes:
	M = 2**p - 1
	Mersenne_primes.append(M)

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	num = int(test)
	M_list = []
	for i in Mersenne_primes:
		if i < num:
			M_list.append(i)
		else:
			break
	M_list = ", ".join(map(str, M_list))
	print M_list

#test_cases.close()