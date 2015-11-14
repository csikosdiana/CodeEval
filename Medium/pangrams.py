data = ['A quick brown fox jumps over the lazy dog', 'A slow yellow fox crawls under the proactive dog']

import string
#print string.ascii_lowercase
#print string.ascii_uppercase

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	sentence = test.lower()
	P = ''
	for l in string.ascii_lowercase:
		if l not in sentence:
			P = P + l
	if P == '':
		print 'NULL'
	else:
		print P

#test_cases.close()