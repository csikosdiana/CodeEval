data = ["2,the",
		"4,lamb its fleece",
		"4,school And so"]

TEXT = "Mary had a little lamb its fleece was white as snow And everywhere that Mary went the lamb was sure to go It followed her to school one day which was against the rule It made the children laugh and play to see a lamb at school And so the teacher turned it out but still it lingered near And waited patiently about till Mary did appear Why does the lamb love Mary so the eager children cry Why Mary loves the lamb you know the teacher did reply"
TEXT = TEXT.split(" ")

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	l = int(test[0]) - 1
	pattern = test[1].split(" ")
	Words = {}
	Total = 0
	i = 0
	while i < len(TEXT) - l:
		if TEXT[i:(i+l)] == pattern:
			Total += 1
			if TEXT[i+l] not in Words:
				Words[TEXT[i+l]] = 1
			else:
				Words[TEXT[i+l]] += 1
		i += 1
	
	W = {}
	for k, v in Words.items():
		m = "{0:.3f}".format(round(v / float(Total),3))
		if m not in W:
			W[m] = [k]
		else:
			W[m].append(k)
	#print W
	T = sorted(W, reverse = True)
	#print T
	Result = []
	for i in T:
		if len(W[i]) == 1:
			Result.append(W[i][0] + "," + i)
		else:
			K = sorted(W[i])
			for j in range(len(K)):
				Result.append(K[j] + "," + i)
	print ";".join(Result)

#test_cases.close()
