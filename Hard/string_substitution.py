data = ["10011011001;0110,1001,1001,0,10,11"]

import string
Alph = string.ascii_uppercase
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(";")
	string = test[0]
	translate = test[1].split(",")
	T1 = {}
	T2 = {}
	k = 0
	for i in range(0, len(translate), 2):
		string = string.replace(translate[i], Alph[k])
		T1[translate[i]] = Alph[k]
		T2[Alph[k]] = translate[i+1]
		k += 1

	Result = ""
	for i in string:
		if i in T2:
			Result = Result + T2[i]
		else:
			Result = Result + i
	print Result

#test_cases.close()