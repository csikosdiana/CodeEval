data = ['a b c d', 'a b c d e f g h i j k l m n o p', 'a b c d e f g h i']

import math
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	test = "".join(test)
	N = int(math.sqrt(len(test)))
	Matrix = []
	row = []
	for l in test:
		if len(row) < N:
			row.append(l)
		else:
			Matrix.append(row)
			row = []
			row.append(l)
	Matrix.append(row)
	
	rotated = zip(*Matrix[::-1])
	Rotated_matrix = ''
	for r in rotated:
		Rotated_matrix = Rotated_matrix + "".join(r)
	print " ".join(list(Rotated_matrix))

#test_cases.close()

