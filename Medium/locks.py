data = ["3 1", "100 100"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	N = int(test[0])
	iters = int(test[1])
	doors = ["unlocked"]*N
	for k in range(0, iters-1):
		for i in range(1, len(doors), 2):
			doors[i] = "locked"
		for i in range(2, len(doors), 3):
			if doors[i] == "unlocked":
				doors[i] = "locked"
			else:
				doors[i] = "unlocked"
	if doors[-1] == "unlocked":
		doors[-1] = "locked"
	else:
		doors[-1] = "unlocked"
	
	print doors.count("unlocked")
	

#test_cases.close()