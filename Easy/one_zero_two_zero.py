data = ["1 8",
		"2 4"]

def dec_to_bits(n):
	bits = ''
	while n > 0:
		m = n%2
		n = n // 2
		bits = bits + str(m)
	return bits[::-1]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(" ")
	zeros = int(test[0])
	length = int(test[1])
	Result = 0
	for i in range(1, length + 1):
		n = dec_to_bits(i)
		c = n.count("0")
		if c == zeros:
			Result += 1
	print Result

#test_cases.close()