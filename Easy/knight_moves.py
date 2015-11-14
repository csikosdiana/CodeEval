data = ["g2", "a1", "d6", "e5", "b1"]

letter_code1 = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15, 'g':16, 'h':17}
letter_code2 = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f', 16:'g', 17:'h'}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = list(test)
	letter = test[0]
	number = test[1]
	steps = []
	
	s1 = letter_code1[letter] + 2
	if s1 in letter_code2:
		l1 = letter_code2[s1]
		n1 = int(number) + 1
		if ((n1 < 9) and (n1 > 0)):
			steps.append(l1 + str(n1))
		
		n2 = int(number) - 1
		if ((n2 < 9) and (n2 > 0)):
			steps.append(l1 + str(n2))

	s2 = letter_code1[letter] - 2
	if s2 in letter_code2:
		l2 = letter_code2[s2]
		n1 = int(number) + 1
		if ((n1 < 9) and (n1 > 0)):
			steps.append(l2 + str(n1))
		
		n2 = int(number) - 1
		if ((n2 < 9) and (n2 > 0)):
			steps.append(l2 + str(n2))
	
	s3 = letter_code1[letter] + 1
	if s3 in letter_code2:
		l3 = letter_code2[s3]
		n1 = int(number) + 2
		if ((n1 < 9) and (n1 > 0)):
			steps.append(l3 + str(n1))
		
		n2 = int(number) - 2
		if ((n2 < 9) and (n2 > 0)):
			steps.append(l3 + str(n2))

	s4 = letter_code1[letter] - 1
	if s4 in letter_code2:
		l4 = letter_code2[s4]
		n1 = int(number) + 2
		if ((n1 < 9) and (n1 > 0)):
			steps.append(l4 + str(n1))
		
		n2 = int(number) - 2
		if ((n2 < 9) and (n2 > 0)):
			steps.append(l4 + str(n2))
	
	print " ".join(sorted(steps))

#test_cases.close()