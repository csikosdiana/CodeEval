data = ["To be, or not to be: that is the question.",
		"Whether 'tis nobler in the mind to suffer.",
		"The slings and arrows of outrageous fortune.",
		"Or to take arms against a sea of troubles.",
		"And by opposing end them, to die: to sleep."]

import string
#print string.ascii_lowercase
#print string.ascii_uppercase

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	count = 0
	line = ''
	for l in test:
		if ((l in string.ascii_lowercase) or (l in string.ascii_uppercase)):
			count += 1
			if count % 2 == 1:
				line = line + l.upper()
			else:
				line = line + l.lower()
		else:
			line = line + l
	print line
	

#test_cases.close()