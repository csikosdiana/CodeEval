data = ["Tom exhibited.",
		"Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.",
		"Tom was tugging at a button-hole and looking sheepish.",
		"Two thousand verses is a great many - very, very great many.",
		"Tom's mouth watered for the apple, but he stuck to his work.",
		"123456789A 23456 89B123456789C123456789D123456789E123456789F123456789G",
		"123456789A123456789B123456789C123456789D123456789E1234 6"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if len(test) <= 55:
		print test
	else:
		sentence = test[:40]
		last_space = sentence.rfind(" ")
		if last_space == -1:
			sentence = sentence + "... <Read More>"
			print sentence
		else:
			sentence = sentence[:last_space]
			sentence = sentence + "... <Read More>"
			print sentence
	

#test_cases.close()
