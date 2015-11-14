data = ["78,51,3,5,5,51230",
		"186,75,68,16,539,312",
		"137,135,48,17,461,512",
		"98,22,6,30,524,100",
		"46,18,7,11,9,46"]
		

def number_generator(a, b, c, r, k):
	m = [a]
	for i in range(1, k):
		l = (b * m[i-1] + c) % r
		m.append(l)
	return m

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	nums = test.split(",")
	n = int(nums[0])
	k = int(nums[1])
	a = int(nums[2])
	b = int(nums[3])
	c = int(nums[4])
	r = int(nums[5])
	m = number_generator(a, b, c, r, k)
	for i in range(k, n):
		sort_m = sorted(m)
		s = 0
		while True:
			if s not in sort_m:
				break
			else:
				s += 1
		m.append(s)
		m.pop(0)
	print m[-1]

#test_cases.close()