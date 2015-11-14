data = ["1 1 | 1 2 | 1 4 | 3 2",
		"1 1 | 1 2 | 1 4 | 3 2 | 4 2",
		"1 2 | 1 4 | 2 3 | 3 2 | 3 4",
		"-13 -7 | -1 9 | 20 6 | 19 19 | -15 15 | 18 -17 | 10 -8 | -6 8 | -15 12 | -16 8 | 9 4 | 10 -6 | -18 4 | -15 17"]

		
def v_equation(a, b):
	v = [b[0] - a[0], b[1] - a[1]]
	f = v[1]*a[0] - v[0]*a[1]
	return [v, f]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if len(test) == 0:
		continue
	points = test.split(" | ")
	P = []
	for i in points:
		P.append([int(i.split(" ")[0]), int(i.split(" ")[1])])
	#print P
	L = []
	for i in range(0, len(P)-2):
		for j in range(i+1, len(P)-1):
			V = v_equation(P[i], P[j])
			K = []
			for k in range(len(P)):
				if P[k] != P[i] and P[k] != P[j]:
					if (V[0][1] * P[k][0] - V[0][0] * P[k][1]) == V[1]:
						if i not in K:
							K.append(i)
						if j not in K:
							K.append(j)
						K.append(k)
			if K != []:
				K = sorted(K)
				if K not in L:
					L.append(sorted(K))
			
	
	print len(L)
#test_cases.close()