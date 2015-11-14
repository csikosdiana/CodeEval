data = ["15.94;16.00", "17;16", "35;35", "45;50"]

Cash = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
Text = ["ONE HUNDRED", "FIFTY", "TWENTY", "TEN", "FIVE", "TWO", "ONE", "HALF DOLLAR", "QUARTER", "DIME", "NICKEL", "PENNY"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	PP = int(float(test[0])*100)
	CH = int(float(test[1])*100)
	if CH < PP:
		print "ERROR"
	elif CH == PP:
		print "ZERO"
	else:
		CB = []
		cash_back = CH - PP
		while cash_back > 0:
			for c in Cash:
				if c <= cash_back:
					k = c
					t_id = Cash.index(c)
					CB.append(Text[t_id])
					break
			cash_back = cash_back - k
		print ",".join(CB)

#test_cases.close()
