data = ["10,3", "5,2"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	n = int(test[0])
	m = int(test[1])
	people = range(n)
	executed = []
	i = 0
	j = 0
	while sorted(executed) != people:
		k = people[j]
		if k not in executed:
			i += 1
			if i % m == 0:
				executed.append(k)
		j += 1
		if j == len(people):
			j = 0
		
	executed = map(str, executed)
	print " ".join(executed)

#test_cases.close()