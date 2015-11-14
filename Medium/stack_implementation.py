data = ["1 2 3 4", "10 -2 3 4"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	alternate = []
	i = 0
	while nums != []:
		x = nums.pop()
		if i % 2 == 0:
			alternate.append(x)
		i += 1
		
	print " ".join(alternate)
#test_cases.close()
