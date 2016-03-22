data = ['**** | *co* | *de* | ****',
		'codx | decx',
		'co | dx']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	T = test.split(' | ')
	l1 = len(T)
	l2 = len(T[0])
	code_count = 0
	for i in range(l1-1):
		for j in range(l2-1):
			r1 = [T[i][j], T[i][j+1]]
			r2 = [T[i+1][j], T[i+1][j+1]]
			r = r1 + r2
			if set(r) == set(["c", "o", "d", "e"]):
				code_count += 1
	print code_count

#test_cases.close()