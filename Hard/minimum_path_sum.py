data = ["2",
		"4,6",
		"2,8",
		"3",
		"1,2,3",
		"4,5,6",
		"7,8,9"]
	
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
N = ""
count = 0
for test in data:
	test = test.strip("\n")
	Matrix = []
	if N == "":
		N = int(test)
	else:
		count += 1
		if count == 1:
			M = []
			r = map(int, test.split(","))
			M.append(r + ["X"]*(N-1))
		elif count <= N:
			c = count - 1
			r = ["X"]*c + map(int, test.split(",")) + ["X"]*(N-c-1)
			M.append(r)
		if count == N:
			rows = N
			N = ""
			count = 0
			Matrix = M[::-1]
			#print Matrix
			i = 0
			Diagonals = []
			while i < (rows + rows -1):
				d = []
				for j in Matrix:
					if j[i] != "X":
						d.append(j[i])
				Diagonals.append(d)
				i += 1
			#print Diagonals
			
			S = Diagonals[0]
			for i in range(1, len(Diagonals)):
				V = Diagonals[i]
				if len(V) > len(S):
					T = []
					for j in range(0, len(V)):
						if j == 0:
							t = S[0] + V[0]
							T.append(t)
						elif j < len(V) - 1:
							t = V[j] + min(S[j-1], S[j])
							T.append(t)
						elif j == len(V) - 1:
							t = S[-1] + V[-1]
							T.append(t)
					S = T[:]
				if len(V) < len(S):
					T = []
					for j in range(0, len(V)):
						t = V[j] + min(S[j], S[j+1])
						T.append(t)
					S = T[:]
			print S[-1]

#test_cases.close()