data = ['1 2 3 4 | 3 1 | 4 1',
		'19 11 | 19 21 23 | 31 39 29',
		'11 1 37 35 40 | 28 | 27 44 30 20 14 | 10 38 22 34 27 9 | 31 26 17 | 21 | 13 17 45 41 1 2 | 33 8 43 | 27 42 48 | 33 20 | 3 | 24 32 36 2 9 8 | 3 41 50 14 | 46 3 44 | 32 31 48 8 | 24 26 12 29 43 | 23 16 | 33 37']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	L = test.split(' | ')
	lists = []
	F = {}
	for i in range(len(L)):
		l = L[i].split(' ')
		for j in l:
			if j not in F:
				F[j] = [str(i+1)]
			else:
				F[j].append(str(i+1))
	K = F.keys()
	K = map(int, K)
	K = sorted(K)
	result = []
	for i in K:
		r = ','.join(F[str(i)])
		result.append(':'.join([str(i), r]))
	print '; '.join(result) + ';'

#test_cases.close()