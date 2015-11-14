data = ["11", "20"]

Coins = [5, 3, 1]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	num = int(test)
	count = 0
	while num > 0:
		for i in Coins:
			if i <= num:
				k = i
				break
		count += 1
		num = num - k
	print count
	

#test_cases.close()