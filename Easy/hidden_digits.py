data = ["abcdefghik", "Xa,}A#5N}{xOBwYBHIlH,#W", "(ABW>'yy^'M{X-K}q,", "6240488"]

Code = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j': '9',
		'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9': '9'}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	HV_digits = ''
	for l in test:
		if l in Code:
			HV_digits = HV_digits + Code[l]
	if HV_digits == '':
		print 'NONE'
	else:
		print HV_digits

#test_cases.close()