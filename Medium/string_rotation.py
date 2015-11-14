data = ["Hello,lloHe", "Basefont,tBasefon"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	string1 = test[0]
	string2 = test[1]
	Rotation = False
	for i in range(1, len(string2)-1):
		s = string2[i:] + string2[:i]
		if s == string1:
			Rotation = True
			break
	
	print Rotation

#test_cases.close()