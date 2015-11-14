data = ["banana", "am so uniqe", "a o  o a", "x mgrxrznbl xk voosmo  b", "b   k   py"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	text = test.rstrip()
	repeated = []
	i = 0
	while i < len(text):
		for j in range(i+1, len(text)+1):
			t = text[i:j]
			if t in text[j:]:
				repeated.append(t)
		i += 1
	#print repeated
	maxi = ""
	for r in repeated:
		if r.replace(" ", "") != "":
			if len(r) > len(maxi):
				maxi = r
	Spaces = maxi.replace(" ", "")
	if Spaces == "":
		print "NONE"
	else:
		print maxi

#test_cases.close()