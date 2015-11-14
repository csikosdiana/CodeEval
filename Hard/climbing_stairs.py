data = ["10", "20", "900"]

MAP = {}
def stairs_count1(n):
	global MAP
	if n in MAP:
		return MAP[n]
	if n <= 2:
		return n
	else:
		MAP[n] = stairs_count1(n-1) + stairs_count1(n-2)
		return MAP[n]
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	n = int(test)
	steps = stairs_count1(n)
	print steps

#test_cases.close()