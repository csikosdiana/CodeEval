data = ["330.39991833", "0.001", "14.64530319", "0.25", "254.16991217"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	angle = float(test)
	whole = int(angle)
	frac1 = int((angle % 1) * 60)
	frac2 = int((((angle % 1) * 60) - frac1) * 60)
	A = str(whole) + "."
	f1 = str(frac1)
	if len(f1) == 1:
		A = A + "0" + f1 + "'"
	else:
		A = A + f1 + "'"
	
	f2 = str(frac2)
	if len(f2) == 1:
		A = A + "0" + f2 + '"'
	else:
		A = A + f2 + '"'
	
	print A
	
#test_cases.close()