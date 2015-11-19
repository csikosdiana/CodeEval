data = ["John Sara Tom Susan | 3",
		"John Tom Mary | 5"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	n = int(test[1])
	names = test[0].split(" ")
	while len(names) > 1:
		idx = (n % len(names)) - 1
		del names[idx]
	print names[0]

#test_cases.close()