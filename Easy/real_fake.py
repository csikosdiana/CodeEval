data = ["9999 9999 9999 9999",
		"9999 9999 9999 9993"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	card = test.replace(" ", "")
	card = map(int, list(card))
	SUM = 0
	for i in range(0, 16):
		if i %2 == 0:
			SUM = SUM + (card[i]*2)
		else:
			SUM = SUM + card[i]
	if SUM % 10 == 0:
		print "Real"
	else:
		print "Fake"
	
#test_cases.close()