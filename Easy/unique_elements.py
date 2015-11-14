
data = ['1,1,1,2,2,3,3,4,4', '2,3,4,5,5', '8,8,9,10,11,11,11,12,12,12,13']
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.split(",")
	U_ints = []
	for i in num:
		k = int(i)
		if k not in U_ints:
			U_ints.append(k)
	U_ints = sorted(U_ints)
	uniques = ''
	for i in U_ints:
		uniques = uniques + str(i) + ","
	uniques = uniques[:-1]
	print uniques

#test_cases.close()