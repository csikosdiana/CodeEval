#data = ["1: ([37.788353, -122.387695], [37.829853, -122.294312])",
#		"2: ([37.429615, -122.087631], [37.487391, -122.018967])",
#		"3: ([37.474858, -122.131577], [37.529332, -122.056046])",
#		"4: ([37.532599,-122.218094], [37.615863,-122.097244])",
#		"5: ([37.516262,-122.198181], [37.653383,-122.151489])",
#		"6: ([37.504824,-122.181702], [37.633266,-122.121964])"]

data = ["1: ([37.794243, -122.154686], [37.624021, -122.231290])",
		"2: ([37.492709, -122.114494], [37.769216, -122.130035])",
		"3: ([37.556968, -122.084324], [37.781791, -122.121041])",
		"4: ([37.626999, -122.250887], [37.610671, -122.328094])",
		"5: ([37.456576, -122.176035], [37.476734, -122.151160])",
		"6: ([37.458053, -122.076666], [37.819552, -122.211201])",
		"7: ([37.790471, -122.210539], [37.676745, -122.108641])",
		"8: ([37.632006, -122.322573], [37.567664, -122.344728])",
		"9: ([37.557999, -122.320956], [37.548723, -122.161533])",
		"10: ([37.632915, -122.362585], [37.567135, -122.119849])",
		"11: ([37.697177, -122.251573], [37.774806, -122.234009])",
		"12: ([37.483320, -122.294341], [37.744972, -122.083771])",
		"13: ([37.689849, -122.199820], [37.753667, -122.181182])",
		"14: ([37.775392, -122.177946], [37.444244, -122.265431])",
		"15: ([37.453186, -122.338629], [37.514409, -122.072376])"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
Bridges = {}
for test in data:
	test = test.rstrip()
	if len(test) == 0:
		continue
	test = test.split(":")
	bridge = int(test[0])
	position = test[1].replace("(", "")
	position = position.replace(")", "")
	position = position.replace("[", "")
	position = position.replace("]", "")
	position = position.replace(" ", "")
	position = position.split(",")
	#print bridge
	#print position
	Bridges[bridge] = [[float(position[0]), float(position[1])], [float(position[2]), float(position[3])]]
	
#test_cases.close()

#print Bridges
N = len(Bridges)

def ccw(A, B, C):
	return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def intersect(A, B, C, D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

I = {}
for i in range(1, N):
	if i not in I:
		I[i] = []
	for j in range(i+1, N+1):
		if j not in I:
			I[j] = []
		A = Bridges[i][0]
		B = Bridges[i][1]
		C = Bridges[j][0]
		D = Bridges[j][1]
		if intersect(A, B, C, D) == True:
			if j not in I[i]:
				I[i].append(j)
			if i not in I[j]:
				I[j].append(i)

#print I
Counter = {}
for k, v in I.items():
	Counter[k] = len(v)

while max(Counter.values()) > 0:
	M = max(Counter, key=Counter.get)
	T = Counter[M]
	K = I[M]
	del Counter[M]
	del I[M]
	for k in K:
		I[k].remove(M)
		Counter[k] -= 1
for i in I.keys():
	print i
