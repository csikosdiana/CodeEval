def modulo(N, M):
	while N >= M:
		N = N - M
	return N

data = ['20,6', '2,3']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.split(",")
	N = int(num[0])
	M = int(num[1])
	print modulo(N, M)

#test_cases.close()