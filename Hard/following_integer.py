data = ["115", "842", "8000"]

import itertools
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	n = test
	perm = list(itertools.permutations(test, len(test)))
	NEXT = ""
	while NEXT == "":
		Nums = []
		for p in perm:
			k = "".join(list(p))
			Nums.append(k)
		Nums = list(set(Nums))
		S = sorted(Nums)
		if n in S:
			id = S.index(n)
		else:
			NEXT = S[0]
		if id == len(S) - 1:
			test = n + "0"
			perm = list(itertools.permutations(test, len(test)))
		else:
			NEXT = S[id+1]
	print NEXT

#test_cases.close()