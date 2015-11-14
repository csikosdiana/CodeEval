data = ['zero;two;five;seven;eight;four', 'three;seven;eight;nine;two']

Code = {'zero' : '0', 'one': '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	word = test.split(";")
	digit = ''
	for i in word:
		digit = digit + Code[i]
	print digit

#test_cases.close()