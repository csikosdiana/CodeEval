data = ["Heelo Codevval | Hello Codeeval",
		"hELLO cODEEVAL | Hello Codeeval",
		"Hello Codeeval | Hello Codeeval"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	text_1 = test[0]
	text_2 = test[1]
	bugs = 0
	for i in range(len(text_1)):
		if text_1[i] != text_2[i]:
			bugs += 1
	if bugs == 0:
		print "Done"
	elif bugs <= 2:
		print "Low"
	elif bugs <= 4:
		print "Medium"
	elif bugs <= 6:
		print "High"
	else:
		print "Critical"
	
#test_cases.close()