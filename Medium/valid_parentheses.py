data = ["()", "([)]"]

Code = {")":"(", "]":"[", "}":"{"}
opens = ["(", "[", "{"]
closes = [")", "]", "}"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	p = test.rstrip()
	Valid = True
	Stack = []
	for i in p:
		if i in opens:
			Stack.append(i)
		elif i in closes:
			if Stack == []:
				Valid = False
				break
			else:
				k = Stack.pop()
				if Code[i] != k:
					Valid = False
					break
	if Stack != []:
		Valid = False

	print Valid
	

#test_cases.close()