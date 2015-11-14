data = ['<--<<--<<', '<<>>--><--<<--<<>>>--><', '<-->>']

Arrow1 = '>>-->'
Arrow2 = '<--<<'

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if len(test) < 5:
		print 0
	else:
		count = 0
		i = 0
		while i < len(test) - 4:
			string = test[i:(i+5)]
			if ((string == Arrow1) or (string == Arrow2)):
				count += 1
			i = i + 1
	print count

#test_cases.close()