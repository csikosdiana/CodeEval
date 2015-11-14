data = ["ABbCcc",
		"Good luck in the Facebook Hacker Cup this year!",
		"Ignore punctuation, please :)",
		"Sometimes test cases are hard to make up.",
		"So I just go consult Professor Dalves"]

import string
L = string.ascii_lowercase

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	string1 = test.lower()
	string1 = string1.replace(" ", "")
	string = ''
	for i in string1:
		if i in L:
			string = string + i
	unique = list(set(string))
	counts = []
	for l in unique:
		c = string.count(l)
		counts.append(c)

	C = sorted(counts, reverse=True)
	beauty = 0
	i = 26
	for c in C:
		beauty = beauty + c*i
		i -= 1
	print beauty
	
#test_cases.close()