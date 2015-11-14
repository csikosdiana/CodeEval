data = ['Hello world!', 'JavaScript language 1.8', 'A letter']

import string

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	sentence = list(test)
	for i in range(0, len(sentence)):
		if sentence[i] in string.ascii_lowercase:
			sentence[i] = sentence[i].upper()
		elif sentence[i] in string.ascii_uppercase:
			sentence[i] = sentence[i].lower()
	
	print "".join(sentence)

#test_cases.close()