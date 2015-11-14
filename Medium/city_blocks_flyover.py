data = ["(0,2,4,8,10,13,14,18,22,23,24,33,40,42,44,47,49,53,55,63,66,81,87,91) (0,147,220)",
		"(0,1,2,4) (0,1,3,4,5)",
		"(0,1,3,4,6) (0,1,2,4)"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	streets = test[0][1:-1].split(",")
	streets = map(int, streets)
	avenues = test[1][1:-1].split(",")
	avenues = map(int, avenues)
	helicopter = [streets[-1], avenues[-1]]
	#print helicopter
	blocks = 0
	j = 0
	i = 1
	while i < len(streets):
		y = avenues[j]
		x = float(streets[i])
		m = (helicopter[1] / float(helicopter[0])) * x
		#print m, y
		if m > y:
			blocks += 1
			j += 1
		else:
			if y != int(m):
				j -= 1
			i += 1
		if i == len(streets):
			break
		#print j, blocks
	print blocks
			
#test_cases.close()
