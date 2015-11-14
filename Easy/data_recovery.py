data = ["2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2",
		"programming first The language;3 2 1",
		"programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	unrec = test[0].split(" ")
	code = map(int, test[1].split(" "))
	l = len(unrec)
	rec = ['']*l
	for i in range(1, l+1):
		if i in code:
			k = code.index(i)
			rec[i-1] = unrec[k]
		else:
			rec[i - 1] = unrec[len(unrec) - 1]
	print " ".join(rec)

#test_cases.close()