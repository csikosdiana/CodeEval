data = ["11 | 11",
		"1001 | 0110 | 1001 | 0110",
		"110 | 101 | 111",
		"000 | 000 | 000",
		"111111 | 001001 | 010010 | 111111 | 001001 | 010010"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(" | ")
	#print test
	if "".join(test).count("1") == len("".join(test)):
		print "1x1, 1"
	elif "".join(test).count("0") == len("".join(test)):
		print "1x1, 0"
	else:
		M = []
		for t in test:
			M.append(list(t))
		#print M
		l = len(M)
		for i in range(1, l+1):
			length = []
			for j in range(l-i+1):
				for k in range(l-i+1):
					SUM = 0
					for r in range(j, j+i):
						SUM += M[r][k:k+i].count('1')
					#print SUM
					if SUM not in length:
						length.append(SUM)
			if len(length) == 1:
				#print length[-1]
				print str(i) + "x" + str(i) + "," + " " + str(length[-1])
				break

#test_cases.close()