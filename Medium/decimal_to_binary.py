data = ['2', '10', ' ', '67', '0']

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
	if test == '0':
		print 0
	elif test:
		bits = dec_to_bits(int(test))
		print bits

#test_cases.close()