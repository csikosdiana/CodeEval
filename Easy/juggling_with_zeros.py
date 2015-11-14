data = ['00 0 0 00 00 0', '00 0', '00 0 0 000 00 0000000 0 000', '0 000000000 00 00', '0 000']

def binary_to_dec(n):
	n = n[::-1]
	dec = 0
	i = 0
	while i < len(n):
		dec = dec + int(n[i])*(2**i)
		i += 1
	
	return dec

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	zeros = test.split(" ")
	binary = ''
	i = 0
	while i < len(zeros) - 1:
		if zeros[i] == '00':
			l = len(zeros[i+1])
			binary = binary + '1'*l
		else:
			binary = binary + zeros[i+1]
		
		i += 2

	try:
		binary = binary[binary.index('1'):]
		print binary_to_dec(binary)
	except:
		print 0

#test_cases.close()