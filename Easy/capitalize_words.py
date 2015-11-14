data = ['Hello world', 'javaScript language', '1st thing', '4TEST', 'TEST']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	words = test.split(" ")
	new_words = []
	for w in words:
		cap_word = w[0].upper() + w[1:]
		new_words.append(cap_word)
	print " ".join(new_words)

#test_cases.close()