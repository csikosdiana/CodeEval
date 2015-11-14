data = ["195", "4319"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.rstrip()
	i = 0
	while i < 100:
		n1 = int(num)
		n2 = int(num[::-1])
		s = n1 + n2
		i += 1
		if str(s) == str(s)[::-1]:
			print str(i) + " " + str(s)
			break
		else:
			num = str(s)

#test_cases.close()