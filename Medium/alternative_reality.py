data = ["100", "4", "17"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
coins = [1, 5, 10, 25, 50]
for test in data:
	test = test.rstrip()
	money = int(test)
	J = range(money+1)
	T = [1]*len(J)
	for c in coins[1:]:
		new_T = [1]
		for j in range(1, len(J)):
			if J[j] >= c:
				new_T.append(T[j] + new_T[j-c])
			else:
				new_T.append(T[j])
		T = new_T[:]
	print T[-1]

#test_cases.close()