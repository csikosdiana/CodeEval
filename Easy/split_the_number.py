data = ['3413289830 a-bcdefghij', '776 a+bc', '12345 a+bcde', '1232 ab+cd', '90602 a+bcde', '16690 abc-de']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	num = test[0]
	pattern = test[1]
	if '-' in pattern:
		i = pattern.find('-')
		num1 = int(num[:i])
		num2 = int(num[i:])
		print num1 - num2
	else:
		i = pattern.find('+')
		num1 = int(num[:i])
		num2 = int(num[i:])
		print num1 + num2

#test_cases.close()