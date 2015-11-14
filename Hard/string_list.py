data = ["1,aa", "2,ab", "3,pop"]

import itertools
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	choose = int(test[0])
	string = list(test[1])
	S_list = []
	for i in itertools.product(string, repeat = choose): 
		s = "".join(i)
		if s not in S_list:
			S_list.append(s)
	print ",".join(sorted(S_list))

#test_cases.close()