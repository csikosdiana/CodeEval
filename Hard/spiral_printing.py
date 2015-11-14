data = ["3;3;1 2 3 4 5 6 7 8 9",
		"3;3;a b c d e f g h i",
		"3;4;1 2 3 4 5 6 7 8 9 10 11 12"]

def spiral_matrix(M, r, c):
	r_s = 1
	r_e = r
	c_s = 1
	c_e = c
	Spiral = []
	
	while ((r_s <= r_e) and (c_s <= c_e)):
		for i in range(c_s, c_e + 1):
			m = M[r_s-1][i-1]
			Spiral.append(m)
		r_s += 1
		
		for j in range(r_s, r_e + 1):
			m = M[j-1][c_e-1]
			Spiral.append(m)
		c_e -= 1
		
		for i in range(c_e, c_s - 1, -1):
			m = M[r_e-1][i-1]
			Spiral.append(m)
		r_e -= 1
		
		for j in range(r_e, r_s - 1, -1):
			m = M[j-1][c_s-1]
			Spiral.append(m)
		c_s += 1
	
	return Spiral

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.replace(";", " ")
	test = test.split(" ")
	r = int(test[0])
	c = int(test[1])
	matrix = test[2:]
	l = len(matrix)
	M = []
	k = 0
	for i in range(r):
		m = []
		for j in range(c):
			m.append(matrix[k])
			k += 1
		M.append(m)
	Sp = spiral_matrix(M, r, c)
	Sp = Sp[:l]
	print " ".join(Sp)

#test_cases.close()