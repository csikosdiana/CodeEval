data = ["ABA*", "BAA*", "A*A*"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	n = len(test)
	part_1 = test[:(n/2)]
	part_2 = test[(n/2):]
	count = 1
	for i in range(n/2):
		if part_1[i] != "*" and part_2[i] != "*":
			if part_1[i] != part_2[i]:
				count = count*0
				break
			else:
				continue
		elif part_1[i] == "*" and part_2[i] == "*":
			count = count*2
	print count

#test_cases.close()