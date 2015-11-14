data = ["XMJYAUZ;MZJAWXU", "BDCAB;ABCB", "hello world mordor;lord of the rings",
		"XBOCTCBNCUTZXGEXIMJ;PGKZHSSLDVLYZFGCD",
		"PGKZHSSLDVLYZFGCD;XBOCTCBNCUTZXGEXIMJ",
		"MZJAWXU;XMJYAUZ"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	if not test:
		print ""
		continue
	test = test.split(";")
	S1 = test[0]
	S2 = test[1]
	#print S1
	#print S2
	Track = [[0]*(len(S1)+1) for x in range(len(S2)+1)]
	
	for l1 in range(1, len(S2)+1):
		for l2 in range(1, len(S1)+1):
			if S2[l1-1] == S1[l2-1]:
				Track[l1][l2] = Track[l1-1][l2-1] + 1
			else:
				Track[l1][l2] = max(Track[l1-1][l2], Track[l1][l2-1])
	#print Track
	L = Track[-1][-1]
	#print L
	LCS = ""
	i = len(S2)
	j = len(S1)
	S = Track[i][j]
	while S > 0:
		k = Track[i][j-1]
		if k != S:
			LCS = S1[j-1] + LCS
			i -= 1
			j -= 1
			S -= 1
		elif k == S and Track[i-1][j] == S:
			i -= 1
		else:
			j -= 1
	print LCS

#test_cases.close()