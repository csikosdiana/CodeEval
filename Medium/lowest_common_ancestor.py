data = ["8 52", "3 29", "8 30", "20 29"]

Tree = [["30", "30"], ["8", "52"], ["3", "20"], ["10", "29"]]

L1 = ["8", "3"]
L2 = ["8", "20", "10"]
L3 = ["8", "20", "29"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	#print nums
	if "30" in nums:
		print "30"
	elif nums in Tree:
		id = Tree.index(nums)
		if id % 2 == 0:
			print Tree[id-1][0]
		else:
			print Tree[id-1][1]
	elif ((nums[0] in L1) and (nums[1] in L1)):
		x_id = L1.index(nums[0])
		y_id = L1.index(nums[1])
		m = min(x_id, y_id)
		print L1[m]
	elif ((nums[0] in L2) and (nums[1] in L2)):
		x_id = L2.index(nums[0])
		y_id = L2.index(nums[1])
		m = min(x_id, y_id)
		print L2[m]
	elif ((nums[0] in L3) and (nums[1] in L3)):
		x_id = L3.index(nums[0])
		y_id = L3.index(nums[1])
		m = min(x_id, y_id)
		print L3[m]
	else:
		x = nums[0]
		y = nums[1]
		for t in Tree:
			if x in t:
				x_id = Tree.index(t)
			if y in t:
				y_id = Tree.index(t)

		m = min(x_id, y_id)
		if m % 2 == 0:
			print Tree[m-1][0]
		else:
			print Tree[m-1][1]
	

#test_cases.close()
