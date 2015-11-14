data = ["hello 11001", "world 10000", "cba 111"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	word = test[0]
	binary_code = test[1]
	Encrypted = ''
	i = 0
	while i < len(word):
		if binary_code[i] == '1':
			Encrypted = Encrypted + word[i].upper()
		else:
			Encrypted = Encrypted + word[i]
		i += 1
	print Encrypted

#test_cases.close()