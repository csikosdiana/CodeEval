data = ["RIGHT; 4; 4 0 2 0|0 0 0 8|4 0 2 4|2 4 2 2",
		"LEFT; 4; 4 0 2 0|0 0 0 8|4 0 2 4|2 4 2 2",
		"UP; 4; 2 0 2 0|0 2 0 4|2 8 0 8|0 8 0 16",
		"DOWN; 4; 2 0 2 0|0 2 0 4|2 8 0 8|0 8 0 16"]

def right_movement(g, row):
	n = []
	for j in g:
		if j != 0:
			n.append(j)
	if n == []:
		return [0]*row
	else:
		h = []
		n = n[::-1]
		if len(n) == 1:
			h = n
		else:
			i = 0
			while i < len(n)-1:
				if n[i] == n[i+1]:
					h.append(n[i]+n[i+1])
					i += 2
					if i == len(n) - 1:
						h.append(n[i])
				else:
					h.append(n[i])
					i += 1
					if i == len(n) - 1:
						h.append(n[i])
				
		z = row - len(h)
		h = h + [0]*z
		return h
#print right_movement([4, 0, 2, 0], 4)

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split("; ")
	move = test[0]
	row = int(test[1])
	grid1 = test[2].split("|")
	grid = []
	for g in grid1:
		g = map(int, g.split(" "))
		grid.append(g)
	#print grid
	#print move
	Result = []
	if move == "RIGHT":
		new_grid = []
		for g in grid:
			h = right_movement(g, row)
			h = h[::-1]
			new_grid.append(h)
		Result = new_grid
			
	elif move == "LEFT":
		new_grid = []
		for g in grid:
			g = g[::-1]
			h = right_movement(g, row)
			new_grid.append(h)
		Result = new_grid
	
	elif move == "UP":
		new_grid = []
		grid = zip(*grid)
		for g in grid:
			g = list(g)
			g = g[::-1]
			h = right_movement(g, row)
			new_grid.append(h)
		new_grid = zip(*new_grid)
		new_grid = map(list, new_grid)
		Result = new_grid
	
	elif move == "DOWN":
		new_grid = []
		grid = zip(*grid)
		for g in grid:
			g = list(g)
			h = right_movement(g, row)
			h = h[::-1]
			new_grid.append(h)
		new_grid = zip(*new_grid)
		new_grid = map(list, new_grid)
		Result = new_grid
	#print Result
	R = []
	for r in Result:
		k = " ".join(map(str, r))
		R.append(k)
	print "|".join(R)

#test_cases.close()
