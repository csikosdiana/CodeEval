data = ['1111 | 1110',
		'10 | 1100001 | 101']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	G = test.split(' | ')
	nums = []
	for g in G:
		b = g[0]
		i = 1
		while i < len(g):
			if b[i-1] == g[i]:
				b += '0'
			else:
				b += '1'
			i += 1
		d = int(b, 2)
		nums.append(d)
	nums = map(str, nums)
	print ' | '.join(nums)

#test_cases.close()