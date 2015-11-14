data = ['92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19',
		'92,11,30,92,1,11,92,38,92,92,43,92,92,51,92,36,97,92,92,92,43,22,84,92,92',
		'4,79,89,98,48,42,39,79,55,70,21,39,98,16,96,2,10,24,14,47,0,50,95,20,95,48,50,12,42']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	sequence = test.split(",")
	L = len(sequence)
	Counter = {}
	for n in sequence:
		if n in Counter:
			Counter[n] = Counter[n] + 1
		else:
			Counter[n] = 1
	if max(Counter.values()) <= L/2:
		print None
	else:
		R = None
		for k, v in Counter.items():
			if v > L/2:
				R = k
				break
		print R

#test_cases.close()