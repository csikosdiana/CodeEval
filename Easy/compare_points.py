data = ["0 0 1 5", "12 13 12 13", "0 1 0 5"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	O = int(test[0])
	P = int(test[1])
	Q = int(test[2])
	R = int(test[3])

	if ((Q - O == 0) and (R - P == 0)):
		print "here"
	
	elif (Q - O) == 0:
		if (R - P) > 0:
			print "N"
		else:
			print "S"
	
	elif (R - P) == 0:
		if (Q - O) > 0:
			print "E"
		else:
			print "W"
			
	elif ((Q - O > 0) and (R - P > 0)):
		print "NE"
	
	elif ((Q - O < 0) and (R - P > 0)):
		print "NW"
	
	elif ((Q - O < 0) and (R - P < 0)):
		print "SW"
	
	else:
		print "SE"

#test_cases.close()
