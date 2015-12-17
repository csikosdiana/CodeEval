data = ["mke", "mh", "lhsby", "pm"]

import string
L = list(string.ascii_lowercase)
Decoder = {}
for i in range(6):
	Decoder[L[i]] = L[-1*(6-i)]
	Decoder[L[-1*(6-i)]] = L[i]

L = L[6:-6]
for j in range(7):
	Decoder[L[j]] = L[-1*(7-j)]
	Decoder[L[-1*(7-j)]] = L[j]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	result = []
	for l in test:
		result.append(Decoder[l])
	print "".join(result)

#test_cases.close()