data = ["ASADB", "ABCCED", "ABCF", "CAASEBE", "ECBFDEES"]

Board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

def neighbour(r, c):
	N = []
	if r > 0:
		N.append([r-1, c])
	
	if r < 2:
		N.append([r+1, c])

	for j in [-1, 1]:
		if c + j >= 0 and c + j < 4:
			N.append([r, c+j])
	
	return N

Visited = [[0, 0, 0, 0] for i in range(3)]
word = ""

def road(current_pos_x, current_pos_y, current_len, n, max_len):
	global word
	if current_len == max_len:
		return True
	neighbours = neighbour(current_pos_x, current_pos_y)
	for k in neighbours:
		if Board[k[0]][k[1]] == word[n] and Visited[k[0]][k[1]] == 0:
			Visited[k[0]][k[1]] = 1
			X = road(k[0], k[1], current_len+1, n+1, max_len)
			if X:
				return True
			Visited[k[0]][k[1]] = 0
	return False

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	word = test.strip("\n")
	Starts = []
	for j in range(len(Board)):
		for k in range(len(Board[j])):
			if Board[j][k] == word[0]:
				Starts.append([j, k])
	if Starts == []:
		print False
		continue
	Result = False
	#print Starts
	for s in Starts:
		Visited = [[0, 0, 0, 0] for i in range(3)]
		Visited[s[0]][s[1]] = 1
		r = road(s[0], s[1], 1, 1, len(word))
		if r == True:
			Result = True
			break
	print Result
#test_cases.close()