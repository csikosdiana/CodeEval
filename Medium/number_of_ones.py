data = ['10', '22', '56']

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
	test = test.rstrip()
	bits = dec_to_bits(int(test))
	b = list(str(bits))
	b = map(int, b)
	print sum(b)

#test_cases.close()