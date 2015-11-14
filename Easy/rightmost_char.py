data = ['Hello World,r', 'Hello CodeEval,E', 'Hello CodeEval,p', 'TjplIQ17BTnz9YgsGiVc64Ci7CuxYVBBPo8gTH6Wmr qrxpyV8LKi8y4 YTqA5WGF5eHeElGTXuneSza, ']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(",")
	String = "".join(test[0])
	t = test[1]
	pos = String.rfind(t)
	print pos

#test_cases.close()