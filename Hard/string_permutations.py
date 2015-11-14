data = ["hat", "abc", "Zu6"]

import itertools
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	string = test.rstrip()
	#print string
	P = list(itertools.permutations(string, len(string)))
	perm = []
	for p in P:
		k = "".join(list(p))
		perm.append(k)
	print ",".join(sorted(perm))

#test_cases.close()