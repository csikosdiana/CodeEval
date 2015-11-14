data = ["(1,2,3);(2,4,6);(4,5,5);(7,3,11);(9,2,14);(13,7,15);(14,3,17)",
		"(2,22,3);(6,12,10);(15,6,21)",
		"(1,2,6);(9,23,22);(22,6,24);(8,14,19);(23,12,30)"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if len(test) == 0:
		continue
	test = test.replace("(", "")
	test = test.replace(")", "")
	test = test.split(";")
	Buildings = []
	for i in test:
		b = map(int, i.split(","))
		Buildings.append(b)
	Buildings = sorted(Buildings)
	s = Buildings[0][0]
	e = 0
	j = len(Buildings) - 1
	while j > -1:
		if Buildings[j][-1] > e:
			e = Buildings[j][-1]
			j -= 1
		else:
			break
	Result = []
	h0 = 0
	for i in range(s, e + 1):
		B = []
		for b in Buildings:
			if b[2] != i:
				B.append(b)
		Buildings = B[:]
		k = i
		h = 0
		for b in Buildings:
			if i >= b[0] and i <= b[2]:
				if b[1] > h:
					k = i
					h = b[1]
		if h != h0:
			Result.append(str(k))
			Result.append(str(h))
			h0 = h
	print " ".join(Result)

#test_cases.close()