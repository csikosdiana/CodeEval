data = ['64 6e 78 | 100101100 11110',
		'5e 7d 59 | 1101100 10010101 1100111',
		'93 75 | 1000111 1011010 1100010']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	T = test.split(' | ')
	virus = T[0].split(' ')
	antivirus = T[1].split(' ')
	virus = sum([int(i, 16) for i in virus])
	antivirus = sum([int(i, 2) for i in antivirus])
	if antivirus >= virus:
		print True
	else:
		print False
	

#test_cases.close()