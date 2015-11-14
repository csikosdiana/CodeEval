data = ['8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21', '24,13,14,43,41']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	words = []
	nums = []
	for i in test:
		try:
			n = int(i)
			nums.append(i)
		except:
			words.append(i)
	if words == []:
		print ",".join(nums)
	elif nums == []:
		print ",".join(words)
	else:
		print "|".join([",".join(words), ",".join(nums)])

#test_cases.close()