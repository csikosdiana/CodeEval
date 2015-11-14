data = ['2020', '22', '1210']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.rstrip()
	Self_d = ''
	for l in range(0, len(num)):
		if int(num[l]) == num.count(str(l)):
			Self_d = '1'
		else:
			Self_d = '0'
			break
	print Self_d

#test_cases.close()