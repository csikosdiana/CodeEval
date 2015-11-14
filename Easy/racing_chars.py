data = ["#########_##",
		"########C_##",
		"#######_####",
		"######_#C###",
		"#######_C###",
		"#######_####",
		"######C#_###",
		"######C_####",
		"#######_####",
		"#######_####"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
position = 0

for test in data:
	test = test.rstrip()
	if position == 0:
		if "C" in test:
			i = test.index("C")
			position = i
			print test.replace("C", "|")
		else:
			i = test.index("_")
			position = i
			print test.replace("_", "|")
	else:
		if "C" in test:
			i = test.index("C")
			if i < position:
				print test.replace("C", "/")
			elif i == position:
				print test.replace("C", "|")
			else:
				print test.replace("C", "\\")
			position = i
		else:
			i = test.index("_")
			if i < position:
				print test.replace("_", "/")
			elif i == position:
				print test.replace("_", "|")
			else:
				print test.replace("_", "\\")
			position = i

#test_cases.close()
