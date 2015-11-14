data = ["12", "123", "9612"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	#print test
	counter = 0
	if len(test) == 1:
		counter = 1
	elif len(test) == 2:
		if int(test) > 26:
			counter = 1
		else:
			counter = 2
	elif len(test) == 3:
		counter += 1
		if int(test[:2]) <= 26:
			counter += 1
		
		if int(test[1:]) <= 26:
			counter += 1
	elif len(test) == 4:
		counter += 1
		if ((int(test[:2]) <= 26) and (int(test[2:]) <= 26)):
			counter += 3
		elif int(test[:2]) <= 26:
			counter += 1
		elif int(test[2:]) <= 26:
			counter += 1
		
		if int(test[1:3]) <= 26:
			counter += 1
	print counter
	

#test_cases.close()