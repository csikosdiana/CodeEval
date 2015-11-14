data = ["5", "0 2", "6 67", "43 71", "39 107", "189 140",
		"7", "0 0", "-2 2", "-2 0", "1 1", "3 3", "5 2", "4 0", "0"]

from math import sqrt
def euclidean_dist(p1, p2):
	E = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	return E

def closest(lst):
	Mini = float("inf")
	for i in xrange(len(lst) - 1):
		for j in xrange(i+1, len(lst)):
			distance = euclidean_dist(lst[i], lst[j])
			if distance < Mini:
				Mini = distance
	return Mini

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
Points = []
N = ""
count = 0
for test in data:
	test = test.strip("\n")
	if len(test) == 0:
		continue
	if N == "":
		N = int(test)
		continue
	elif N == "0":
		break
	count += 1
	if count < N:
		t = map(int, test.split(" "))
		Points.append((t[0], t[1]))
	else:
		t = map(int, test.split(" "))
		Points.append((t[0], t[1]))
		Points.sort(key = lambda x : (x[0], x[1]))
		P1 = Points[:(N//2)]
		P2 = Points[(N//2):]
		M_P1 = closest(P1)
		M_P2 = closest(P2)
		Min_dist = min(M_P1, M_P2)
		x = (P1[-1][0] + P2[0][0]) // 2
		int_left = x - Min_dist
		int_right = x + Min_dist
		new_Points = []
		for p in Points:
			if p[0] >= int_left and p[0] <= int_right:
				new_Points.append(p)
		m = closest(new_Points)
		if m < Min_dist:
			Min_dist = m
		if Min_dist >= 10000:
			print "INFINITY"
		else:
			print "%.4f" % Min_dist
		Points = []
		count = 0
		N = ""

#test_cases.close()