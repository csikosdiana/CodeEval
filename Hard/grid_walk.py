def Accessible(x, y):
	x = abs(x)
	x_s = sum(map(int, list(str(x))))
	if x_s > 19:
		return False
	y = abs(y)
	y_s = sum(map(int, list(str(y))))
	return (x_s + y_s <= 19)

def neighbors(n):
	x, y = n[0], n[1]
	return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

import collections

visited = {(0, 0)}
walk = collections.deque([(0, 0)])

while len(walk) > 0:
	n = walk.pop()
	for i in neighbors(n):
		if i not in visited and Accessible(i[0], i[1]) == True:
			visited.add(i)
			walk.append(i)
print len(visited)
