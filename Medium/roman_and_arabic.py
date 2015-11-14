data = ["3M1D2C", "2I3I2X9V1X", "3X2I4X"]

RtoA = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	aromatic = test.rstrip()
	value = 0
	for i in range(0, len(aromatic), 2):
		a = int(aromatic[i])
		r = RtoA[aromatic[i+1]]
		if i <= len(aromatic) - 3:
			if r < RtoA[aromatic[i+3]]:
				value = value - a*r
			else:
				value = value + a*r
		else:
			value = value + a*r
	print value

#test_cases.close()