data = ['(--9Hello----World...--)', 'Can 0$9 ---you~', '13What213are;11you-123+138doing7']


import string
print string.ascii_lowercase
print string.ascii_uppercase

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	l = len(test)
	sentence = ''
	for c in range(0, l):
		char = test[c]
		if ((char in string.ascii_lowercase) or (char in string.ascii_uppercase)):
			sentence = sentence + char
		else:
			sentence = sentence + " "
	sentence = " ".join(sentence.split())
	print sentence.lower()

#test_cases.close()
