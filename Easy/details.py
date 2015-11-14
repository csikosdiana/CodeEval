data = ['XX.YY,XXX.Y,X..YY,XX..Y',
		'XXX.YYYY,X...Y..Y,XX..YYYY,X.....YY,XX....YY',
		'XX...YY,X....YY,XX..YYY,X..YYYY',
		'XXYY,X..Y,XX.Y']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	dist = []
	for i in test:
		x = i.rfind("X")
		y = i.index("Y")
		d = y - x - 1
		dist.append(d)
	print min(dist)


#test_cases.close()