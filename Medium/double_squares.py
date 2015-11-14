data = ["5", "10", "25", "3", "0", "1"]


import math
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
c = 0
for test in data:
	test = test.rstrip()
	if c == 0:
		N = int(test)
		c = 1
	else:
		num = int(test)
		#print num
		count = []
		i = 0
		while i < int(math.sqrt(num)) + 1:
			s = num - i**2
			if s >= 0:
				sr = int(math.sqrt(s))
				if s == sr*sr:
					if sr not in count:
						count.append(i)
						count.append(sr)
			i += 1
		print len(count) / 2
	
#test_cases.close()