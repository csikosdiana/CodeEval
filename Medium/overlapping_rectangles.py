data = ["-3,3,-1,1,1,-1,3,-3", "-3,3,-1,1,-2,4,2,2"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	nums = map(int, test)
	A1 = [nums[0], nums[1]]
	A2 = [nums[2], nums[3]]
	B1 = [nums[4], nums[5]]
	B2 = [nums[6], nums[7]]
	
	Points = []
	for i in range(A1[0], A2[0]+1):
		for j in range(A1[1], A2[1]-1, -1):
			Points.append([i, j])
	
	Result = False
	for i in range(B1[0], B2[0]+1):
		for j in range(B1[1], B2[1]-1, -1):
			if [i, j] in Points:
				Result = True
				break
		if Result == True:
			break
	print Result

#test_cases.close()