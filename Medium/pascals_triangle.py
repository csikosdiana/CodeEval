data = ['6', '5', '8', '1', '2']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	#print test
	depth = int(test)
	Result = ''
	
	if depth == 1:
		Result = '1'
	elif depth == 2:
		Result = " ".join(['1', '1', '1'])
	else:

		k = [1, 1]
		Pascal = [[1], k]
		for i in range(2, depth):
			p = [1]
			for i in range(2, len(k)+1):
				t = k[i-1] + k[i-2]
				p.append(t)
			p.append(1)
			k = p
			Pascal.append(k)
		P_T = []
		for p in Pascal:
			p = map(str, p)
			p = " ".join(p)
			P_T.append(p)
		Result = " ".join(P_T)
	
	print Result

#test_cases.close()