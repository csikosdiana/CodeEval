data = ['how are you, abc', 'hello world, def']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(", ")
	sentence = test[0]
	for c in test[1]:
		sentence = sentence.replace(c, "")
	print sentence

#test_cases.close()

