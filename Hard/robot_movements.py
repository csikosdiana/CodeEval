GRID = [[False]*4 for i in range(4)]

def move(position_x, position_y, end_x, end_y):
	global GRID
	if ((position_x < 0) or (position_x > 3)):
		return 0
	if ((position_y < 0) or (position_y > 3)):
		return 0
	if GRID[position_x][position_y] == True:
		return 0
	if ((position_x == end_x) and (position_y == end_y)):
		return 1
	GRID[position_x][position_y] = True
	
	movements = 0
	
	movements += move(position_x - 1, position_y, end_x, end_y)
	movements += move(position_x + 1, position_y, end_x, end_y)
	movements += move(position_x, position_y - 1, end_x, end_y)
	movements += move(position_x, position_y + 1, end_x, end_y)
	
	GRID[position_x][position_y] = False
	return movements
	

print move(0,0,3,3)
