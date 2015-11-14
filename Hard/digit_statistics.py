data = ["2 5", "3 4", "6 15", "352 4034"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	a = int(test[0])
	n = int(test[1])
	ends = []
	i = 1
	while True:
		k = a**i
		k = k % 10
		if k not in ends:
			ends.append(k)
		else:
			break
		i += 1

	statistics = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	l = n // len(ends)

	for e in ends:
		statistics[e] = l
	
	h = n % len(ends)

	for i in range(0, h):
		statistics[ends[i]] = statistics[ends[i]] + 1
	
	Result = []
	for k, v in statistics.items():
		Result.append(str(k) + ": " + str(v))
	print ", ".join(Result)
	

#test_cases.close()
