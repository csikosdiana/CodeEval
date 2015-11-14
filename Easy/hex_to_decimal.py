data = ['9f', '11', '7de']

Numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a': 10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	h = list(test)
	h = h[::-1]
	D = 0
	for i in range(0, len(h)):
		k = Numbers[h[i]]*(16**i)
		D = D + k
	print D

#test_cases.close()