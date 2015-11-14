data = ["Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)",
		"Center: (5.05, -11); Radius: 21.2; Point: (-31, -45)",
		"Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)",
		"Center: (40.26, -36.47); Radius: 39; Point: (-40, -13.56)"]

import math
def euclidean_dist(p1, p2):
	E = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
	return E

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	Center = test[0]
	Center = Center.replace("(", "")
	Center = Center.replace(")", "")
	Center = Center.replace(",", "")
	Center = Center.split(" ")
	C = [Center[1], Center[2]]
	Radius = test[1]
	Radius = Radius.split(" ")
	R = Radius[2]
	Point = test[2]
	Point = Point.replace("(", "")
	Point = Point.replace(")", "")
	Point = Point.replace(",", "")
	Point = Point.split(" ")
	P = [Point[2], Point[3]]
	
	C = map(float, C)
	R = float(R)
	P = map(float, P)
	if euclidean_dist(C, P) <= R:
		print "true"
	else:
		print "false"

#test_cases.close()