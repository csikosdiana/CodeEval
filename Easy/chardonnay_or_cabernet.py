data = ["Cabernet Merlot Noir | ot",
		"Chardonnay Sauvignon | ann",
		"Shiraz Grenache | o"]
		
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	wines = test[0].split(" ")
	part = test[1]
	WINE = []
	i = 0
	while i < len(wines):
		R = True
		w = wines[i]
		for l in part:
			c = part.count(l)
			if c > w.count(l):
				R = False
		if R == True:
			WINE.append(w)
		i += 1
	if WINE == []:
		print False
	else:
		print " ".join(WINE)

#test_cases.close()