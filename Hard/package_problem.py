data = ["81 : (1,53.38,$45) (2,88.62,$98) (3,78.48,$3) (4,72.30,$76) (5,30.18,$9) (6,46.34,$48)",
		"8 : (1,15.3,$34)",
		"75 : (1,85.31,$29) (2,14.55,$74) (3,3.98,$16) (4,26.24,$55) (5,63.69,$52) (6,76.25,$75) (7,60.02,$74) (8,93.18,$35) (9,89.95,$78)",
		"56 : (1,90.72,$13) (2,33.80,$40) (3,43.15,$10) (4,37.97,$16) (5,46.81,$36) (6,48.77,$79) (7,81.80,$45) (8,19.36,$79) (9,6.76,$64)"]

from itertools import combinations
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if len(test) == 0:
		continue
	test = test.split(" : ")
	W_LIMIT = float(test[0])
	#print W_LIMIT
	data = test[1].replace("(", "")
	data = data.replace(")", "")
	data = data.replace("$", "")
	data = data.split(" ")
	#print data
	WEIGHTS = {}
	COSTS = {}
	for d in data:
		d = d.split(",")
		if float(d[1]) <= W_LIMIT:
			i = int(d[0])
			WEIGHTS[i] = float(d[1])
			COSTS[i] = float(d[2])
	#print WEIGHTS
	#print COSTS
	if WEIGHTS == {}:
		print "-"
		continue
	W = sorted(WEIGHTS, key = WEIGHTS.get, reverse = True)
	C = sorted(COSTS, key = COSTS.get, reverse = True)
	MAX_COST = COSTS[C[0]]
	MIN_W = W_LIMIT
	Packages = [C[0]]
	#print MAX_COST
	#print Packages
	for k in xrange(2, len(W)):
		L = list(combinations(W, k))
		for lst in L:
			wh = 0
			ch = 0
			for t in lst:
				wh += WEIGHTS[t]
				ch += COSTS[t]
			if wh <= W_LIMIT:
				if ch == MAX_COST:
					if wh < MIN_W:
						MAX_COST = ch
						MIN_W = wh
						Packages = lst
				if ch > MAX_COST:
					MAX_COST = ch
					MIN_W = wh
					Packages = lst
	print ",".join(map(str, sorted(Packages)))

#test_cases.close()
