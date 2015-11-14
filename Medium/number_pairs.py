data = ['1,2,3,4,6;5', '2,4,5,6,9,11,15;20', '1,2,3,4;50']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	nums = map(int, test[0].split(","))
	sum = int(test[1])
	i = 0
	Pairs = []
	while i < len(nums):
		if sum - nums[i] in nums[(i+1):]:
			P = sorted([nums[i], sum - nums[i]])
			if P not in Pairs:
				Pairs.append(P)
		i += 1
	if Pairs == []:
		print 'NULL'
	else:
		str_p = []
		for i in Pairs:
			i = map(str, i)
			str_p.append(",".join(i))
		print ";".join(str_p)

#test_cases.close()