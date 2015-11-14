data = ["100 Lower Lower Higher Lower Lower Lower Yay!",
		"500 Yay!",
		"948 Higher Lower Yay!",
		"557 Lower Lower Lower Yay!",
		"917 Lower Lower Lower Lower Higher Yay!"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	upper_bound = int(test[0])
	lower_bound = 0
	hints = test[1:]
	l = lower_bound + upper_bound
	g = l / 2
	if l % 2 == 1:
		g = g + 1
	for h in hints:
		if h == "Lower":
			l = lower_bound + upper_bound
			g = l / 2
			if l % 2 == 1:
				g = g + 1
			upper_bound = g - 1
		elif h == "Higher":
			l = lower_bound + upper_bound
			g = l / 2
			if l % 2 == 1:
				g = g + 1
			lower_bound = g + 1
		elif h == "Yay!":
			l = lower_bound + upper_bound
			g = l / 2
			if l % 2 == 1:
				g = g + 1
			print g

#test_cases.close()

