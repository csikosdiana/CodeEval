data = ['86,2,3', '125,1,2']

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
	l = test.split(",")
	dec_num = int(l[0])
	bits_num = dec_to_bits(dec_num)
	
	i = int(l[1]) - 1
	j = int(l[2]) - 1
	K = list(bits_num[::-1])
	if K[i] == K[j]:
		print 'true'
	else:
		print 'false'

#test_cases.close()