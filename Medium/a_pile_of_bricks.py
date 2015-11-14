data = ["[4,3] [3,-3]|(1 [10,9,4] [9,4,2])",
		"[-1,-5] [5,-2]|(1 [4,7,8] [2,9,0]);(2 [0,7,1] [5,9,8])",
		"[-4,-5] [-5,-3]|(1 [4,8,6] [0,9,2]);(2 [8,-1,3] [0,5,4])",
		"[16,28] [91,1]|(1 [57,-76,-10] [-51,-62,49]);(2 [29,-32,15] [-77,73,-27]);(3 [-56,-61,28] [-38,23,72]);(4 [-36,-15,76] [-68,83,-87]);(5 [68,57,-72] [-10,-4,70]);(6 [-38,9,92] [75,-62,96]);(7 [-3,3,90] [-66,-52,-10]);(8 [52,100,-43] [-14,8,46]);(9 [-43,5,-48] [21,99,84]);(10 [-9,-95,23] [-54,-80,-5]);(11 [-13,67,-3] [-59,84,-46])"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	if test:
		test = test.rstrip()
		test = test.split("|")
		hole = test[0].replace("[", "")
		hole = hole.replace("]", "")
		hole = hole.replace(",", " ")
		hole = map(int, hole.split(" "))
		min_x = abs(hole[0] - hole[2])
		min_y = abs(hole[1] - hole[3])
		#print min_x, min_y
		Pass = []
		bricks = test[1].split(";")
		for b in range(0, len(bricks)):
			r = bricks[b]
			j = r.index("[")
			r = r[j:-1]
			r = r.replace("[", "")
			r = r.replace("]", "")
			r = r.replace(",", " ")
			r = map(int, r.split(" "))
			x = abs(r[0] - r[3])
			y = abs(r[1] - r[4])
			z = abs(r[2] - r[5])
			count = 0
			H = [min_x, min_y]
			B = [x, y, z]
			#print H, B
			while len(H) > 0:
				m1 = min(H)
				m2 = min(B)
				if m2 <= m1:
					count += 1
					H.remove(m1)
					B.remove(m2)
				else:
					break
			if count == 2:
				Pass.append(b+1)
		if Pass == []:
			print "-"
		else:
			Pass = map(str, Pass)
			print ",".join(Pass)

#test_cases.close()

