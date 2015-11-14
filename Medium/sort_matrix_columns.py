data = ["-3 29 -3 | -17 69 -17 | 44 3 8",
		"25 39 -26 -21 | -81 -98 -91 27 | 32 -87 67 98 | -90 -79 18 9",
		"26 -10 39 | -62 66 97 | 22 85 36"]

def multi_counter(l):
	m = []
	for i in range(0, len(l)):
		if l.count(l[i]) > 1:
			m.append(i)
	return m

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	rows = test.split(" | ")
	R = []
	for r in rows:
		r = map(int, r.split(" "))
		R.append(r)
	i = 0
	X = R[0]
	while i < len(R)-1:
		if X[i] > X[i+1]:
			X[i], X[i+1] = X[i+1], X[i]
			for j in range(1, len(R)):
				R[j][i], R[j][i+1] = R[j][i+1], R[j][i]
			if i > 0:
				i -= 1
		else:
			i += 1
	#print R
	
	for i in range(0, len(R) - 1):
		m = multi_counter(R[i])
		if m == []:
			break
		else:
			#print m
			if R[i+1][m[0]] > R[i+1][m[1]]:
				R[i+1][m[0]], R[i+1][m[1]] = R[i+1][m[1]], R[i+1][m[0]]
				for j in range(i+2, len(R)):
					R[j][m[0]], R[j][m[1]] = R[j][m[1]], R[j][m[0]]
				break

	#print R
	new_R = []
	for r in R:
		ordr = map(str, r)
		ordr = " ".join(ordr)
		new_R.append(ordr)
	print " | ".join(new_R)
					
#test_cases.close()
