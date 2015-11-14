data = ["1 2 | 6 7 | 7 2 | 1 6 | 2 3",
		"1 2 | 6 7 | 7 2 | 1 6 | 2 3 | 7 8 | 3 8",
		"1 2 | 1 6 | 6 7",
		"1 2 | 6 7 | 7 2 | 1 6 | 2 3 | 3 8 | 6 11 | 11 12 | 13 12 | 8 13"]

M = {}
for i in xrange(1, 25, 5):
	for j in xrange(i, i + 4):
		M[(j, j + 1)] = False

for j in xrange(1, 21):
	M[(j, j+5)] = False

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if len(test) == 0:
		continue
	MAP = dict(M)
	test = test.split(" | ")
	for t in test:
		t = map(int, t.split(" "))
		t = sorted(t)
		MAP[(t[0], t[1])] = True
	Counter = 0
	for i in xrange(1, 20):
		Rectangle = True
		if i % 5 != 0:
			if MAP[(i, i+1)] == False:
				Rectangle = False
			elif MAP[(i+1, i+6)] == False:
				Rectangle = False
			elif MAP[(i+5, i+6)] == False:
				Rectangle = False
			elif MAP[(i, i+5)] == False:
				Rectangle = False
			
			if Rectangle == True:
				Counter += 1
	for j in [1, 2, 3, 6, 7, 8, 11, 12, 13]:
		Rectangle = True
		if MAP[(j, j+1)] == False:
			Rectangle = False
		elif MAP[(j+1, j+2)] == False:
			Rectangle = False
		elif MAP[(j+2, j+7)] == False:
			Rectangle = False
		elif MAP[(j+7, j+12)] == False:
			Rectangle = False
		elif MAP[(j, j+5)] == False:
			Rectangle = False
		elif MAP[(j+5, j+10)] == False:
			Rectangle = False
		elif MAP[(j+10, j+11)] == False:
			Rectangle = False
		elif MAP[(j+11, j+12)] == False:
			Rectangle = False
		
		if Rectangle == True:
				Counter += 1
	
	for i in [1, 2, 6, 7]:
		Rectangle = True
		if MAP[(i, i+1)] == False:
			Rectangle = False
		elif MAP[(i+1, i+2)] == False:
			Rectangle = False
		elif MAP[(i+2, i+3)] == False:
			Rectangle = False
		elif MAP[(i+3, i+8)] == False:
			Rectangle = False
		elif MAP[(i+8, i+13)] == False:
			Rectangle = False
		elif MAP[(i+13, i+18)] == False:
			Rectangle = False
		elif MAP[(i, i+5)] == False:
			Rectangle = False
		elif MAP[(i+5, i+10)] == False:
			Rectangle = False
		elif MAP[(i+10, i+15)] == False:
			Rectangle = False
		elif MAP[(i+15, i+16)] == False:
			Rectangle = False
		elif MAP[(i+16, i+17)] == False:
			Rectangle = False
		elif MAP[(i+17, i+18)] == False:
			Rectangle = False
		
		if Rectangle == True:
				Counter += 1
	
	Rectangle = True
	k = 1
	while k < 5:
		if MAP[(k, k + 1)] == False:
			Rectangle = False
		k += 1
	if Rectangle == False:
		print Counter
		continue
	k = 5
	while k < 25:
		if MAP[(k, k + 5)] == False:
			Rectangle = False
		k += 5
	if Rectangle == False:
		print Counter
		continue
	
	k = 1
	while k < 20:
		if MAP[(k, k + 5)] == False:
			Rectangle = False
		k += 5
	if Rectangle == False:
		print Counter
		continue
	
	k = 21
	while k < 25:
		if MAP[(k, k + 1)] == False:
			Rectangle = False
		k += 1
	if Rectangle == False:
		print Counter
		continue
	
	if Rectangle == True:
		Counter += 1
	print Counter
	
#test_cases.close()