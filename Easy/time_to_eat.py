data = ["02:26:31 14:44:45 09:53:27",
		"05:33:44 21:25:41"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(" ")
	print " ".join(sorted(test)[::-1])

#test_cases.close()