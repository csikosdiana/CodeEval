data = ["soup,sugar,peas,rice",
		"ljhqi,nrtxgiu,jdtphez,wosqm",
		"cjz,tojiv,sgxf,awonm,fcv"]

def chain(start, words):
    remaining = list(words)
    del remaining[remaining.index(start)]
    possibles = [x for x in remaining if x[:1] == start[-1:]]
    maxchain = []
    for c in possibles:
        l = chain(c, remaining)
        if len(l) > len(maxchain):
            maxchain = l
    return [start] + maxchain

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	words = test.split(",")
	if len(test) == 0:
		continue
	MAX_chain = 0
	for w in words:
		CH = chain(w, words)
		if len(CH) > MAX_chain:
			MAX_chain = len(CH)
	if MAX_chain == 1:
		print None
	else:
		print MAX_chain

#test_cases.close()