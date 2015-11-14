data = ['(1,6), (6,7), (2,7), (9,1)', '(4,1), (3,4), (0,5), (1,2)', '(4,6), (5,5), (5,6), (4,5)', '(2,2), (2,2), (2,2), (2,2)']
import math
def euclidean_dist(p1, p2):
	E = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	return E

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.replace("(", "")
	test = test.replace(")", "")
	test = test.replace(" ", "")
	C = test.split(",")
	C = map(int, C)
	#print C

	x = []
	y = []
	for i in range(0, len(C)):
		if i% 2 == 0:
			x.append(C[i])
		else:
			y.append(C[i])

	Points = dict()
	m = min(x)
	id = x.index(m)
	s1 = [x[id], y[id]]
	x.remove(x[id])
	y.remove(y[id])
	
	m = min(x)
	id = x.index(m)
	s2 = [x[id], y[id]]
	x.remove(x[id])
	y.remove(y[id])
	
	
	if s1[1] < s2[1]:
		Points[1] = s1
		Points[2] = s2
	else:
		Points[1] = s2
		Points[2] = s1
	
	s3 = [x[0], y[0]]
	s4 = [x[1], y[1]]
	
	if s3[1] > s4[1]:
		Points[3] = s3
		Points[4] = s4
	else:
		Points[3] = s4
		Points[4] = s3
	#print Points
	if ((s1 == s2) or (s1 == s3) or (s1 == s4) or (s2 == s3) or (s2 == s4) or (s3 == s4)):
		print "false"
		continue
	a = euclidean_dist(Points[1], Points[2])
	b = euclidean_dist(Points[2], Points[3])
	c = euclidean_dist(Points[3], Points[4])
	d = euclidean_dist(Points[4], Points[1])
	e = euclidean_dist(Points[1], Points[3])
	f = euclidean_dist(Points[2], Points[4])
	if ((a == b == c == d) and (e == f)):
		print "true"
	else:
		print "false"

#test_cases.close()
