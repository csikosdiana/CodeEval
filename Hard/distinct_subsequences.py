data = ["babgbag,bag",
		"rabbbit,rabbit"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(",")
	string = test[0]
	substring = test[1]
	D = {}
	for i in substring:
		D[i] = []
	for i in range(len(string)):
		if string[i] in D:
			D[string[i]].append(i)
	#print D
	Results = []
	for l in substring:
		if Results == []:
			for i in D[l]:
				Results.append([i])
		else:
			R = []
			for r in Results:
				for i in D[l]:
					if i > r[-1]:
						R.append(r[:] + [i])
			Results = R[:]
	new_Results = []
	for r in Results:
		if len(r) == len(substring):
			new_Results.append(r)
	print len(new_Results)
		

#test_cases.close()