data = ['some line with text', 'another line']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	l = test.split(" ")
	longest = ''
	max_len = 0
	for i in l:
		length = len(i)
		if length > max_len:
			max_len = length
			longest = i
	print longest

#test_cases.close()