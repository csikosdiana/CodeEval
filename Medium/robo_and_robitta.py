data = ["3x2 | 2 1", "4x4 | 3 3", "8x4 | 7 1", "13x5 | 12 4"]

def spiral_matrix(r, c, goal_r, goal_c):
	r_s = 1
	r_e = r
	c_s = 1
	c_e = c
	
	goal = []
	nuts_count = 0
	NUTS = 0
	
	while ((r_s <= r_e) and (c_s <= c_e)):
		for i in range(c_s, c_e + 1):
			goal = [r_s, i]
			nuts_count += 1
			if goal == [goal_r, goal_c]:
				NUTS = nuts_count
				return NUTS
		r_s += 1
		
		for j in range(r_s, r_e + 1):
			goal = [j, c_e]
			nuts_count += 1
			if goal == [goal_r, goal_c]:
				NUTS = nuts_count
				return NUTS
		c_e -= 1
		
		for i in range(c_e, c_s - 1, -1):
			goal = [r_e, i]
			nuts_count += 1
			if goal == [goal_r, goal_c]:
				NUTS = nuts_count
				return NUTS
		r_e -= 1
		
		for j in range(r_e, r_s - 1, -1):
			goal = [j, c_s]
			nuts_count += 1
			if goal == [goal_r, goal_c]:
				NUTS = nuts_count
				return NUTS
		c_s += 1

	return nuts_count

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	matrix = map(int, test[0].split("x"))
	date = map(int, test[1].split(" "))
	k = matrix[1] - date[1] + 1
	nuts = spiral_matrix(matrix[1], matrix[0], k, date[0])
	print nuts

#test_cases.close()
