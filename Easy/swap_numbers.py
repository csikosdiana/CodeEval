data = ['4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5', '5Nobody5 7expects3 5the4 6Spanish4 9inquisition0', '6Well8 1she2 7turned7 0me6 6into3 6a3 0newt8        ']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	l1 = ' '.join(test.split())
	l = l1.split(" ")
	swaped = []
	for t in l:
		k = t[len(t)-1] + t[1:len(t)-1] + t[0]
		swaped.append(k)
	print " ".join(swaped)

#test_cases.close()