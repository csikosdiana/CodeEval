data = [":((",
		"i am sick today (:()",
		"(:)",
		"hacker cup: started :):)",
		")(",
		"(:a))",
		"bbb:(a b)ccc  :::(aaa(: (cab(bccaa(:cb):a: bc):::(cba)b()c)::((a cb))bcb:  c:bb::c:(::)())"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	t = test.rstrip()
	minOpen = 0
	maxOpen = 0
	i = 0
	while i < len(t):
		if t[i] == "(":
			maxOpen += 1
			if ((i == 0) or (t[i-1] != ":")):
				minOpen += 1
		elif t[i] == ")":
			minOpen = max(0, minOpen-1)
			if ((i == 0) or (t[i-1] != ":")):
				maxOpen -= 1
				if maxOpen < 0:
					break
		i += 1
	if ((maxOpen >= 0) and (minOpen == 0)):
		print "YES"
	else:
		print "NO"

#test_cases.close()