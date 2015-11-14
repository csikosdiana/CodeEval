data = ['9 0 6 | 15 14 9', '5 | 8', '13 4 15 1 15 5 | 1 4 15 14 8 2']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	list1 = test[0].split(" ")
	list1 = map(int, list1)
	list2 = test[1].split(" ")
	list2 = map(int, list2)
	multi = []
	for i in range(0, len(list1)):
		m = list1[i]*list2[i]
		multi.append(m)
	multi = map(str, multi)
	print " ".join(multi)

#test_cases.close()