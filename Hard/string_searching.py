data = ['Hello,ell', 'This is good, is', 'CodeEval,C*Eval', 'Old,Young', 'CwWnfpM1YFYnNMPGNl03ptiI,03p*', 'MOjVRg*O7fycj,OjVRg\*']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	#print test
	test = test.split(",")
	string = test[0]
	subs = test[1]
	Result = ''
	if '*' not in subs:
		if subs in string:
			Result = 'true'
		else:
			Result = 'false'
	else:
		if '\*' in subs:
			subs = subs.replace('\*', '*')
			if subs in string:
				Result = 'true'
			else:
				Result = 'false'
		elif subs[len(subs)-1] == '*':
			if subs[:len(subs)-1] in string:
				Result = 'true'
			else:
				Result = 'false'
		else:
			subs = subs.split("*")
			try:
				i = string.find(subs[0])
				j = string.find(subs[1])
				if i < j:
					Result = 'true'
				else:
					Result = 'false'
			except:
				Result = 'false'
	print Result

#test_cases.close()