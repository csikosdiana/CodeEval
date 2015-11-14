data = ["5;0,1,2,3,0", "20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	if test:
		test = test.rstrip()
		test = test.split(";")
		length = int(test[0])
		nums = map(int, test[1].split(","))
		for i in range(0, length):
			c = nums.count(i)
			if c == 2:
				print i
				break
	

#test_cases.close()