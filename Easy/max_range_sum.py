data = ["5;7 -3 -10 4 2 8 -2 4 -5 -2", "6;-4 3 -10 5 3 -7 -3 7 -6 3", "3;-7 0 -45 34 -24 7"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	days = int(test[0])
	g_l = test[1].split(" ")
	g_l = map(int, g_l)
	Max_gain = 0
	i = 0
	while i < len(g_l) - (days - 1):
		S = sum(g_l[i:(i+days)])
		if S > Max_gain:
			Max_gain = S
		i = i + 1
	print Max_gain

#test_cases.close()