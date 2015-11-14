data = ["fifteen",
		"negative six hundred thirty eight",
		"zero",
		"two million one hundred seven",
		"fourteen million one hundred twelve thousand sixty",
		"six hundred eleven million",
		"forty one million one hundred twelve thousand sixty"]

Numbers = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
			"ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
			"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	if test in Numbers:
		print Numbers[test]
		continue
	Result = 0
	Neg = False
	if test.startswith("negative"):
		Neg = True
		idx = test.index(" ")
		test = test[(idx+1):]
	#print test, Neg
	M = test.split(" million")
	if len(M) != 1:
		N = M[0].split(" ")
		if len(N) == 1:
			Result += Numbers[N[0]] * 1000000
		elif "hundred" not in N:
			Result += (Numbers[N[0]] + Numbers[N[1]]) * 1000000
		else:
			N = N[::-1]
			R = 0
			i = 0
			while i < len(N):
				if N[i] in Numbers:
					R += Numbers[N[i]]
				elif N[i] == "hundred":
					h = 100
					e = Numbers[N[i+1]]
					if i+2 < len(N):
						t = Numbers[N[i+2]]
						R += (t+e)*h
						i += 2
					else:
						R += e*h
						i += 1
				i += 1
						
			Result += R * 1000000
	
	if len(M) > 1:
		M = M[1:]
	if M[0].startswith(" "):
		M[0] = M[0][1:]
	T = M[0].split(" thousand")
	if len(T) != 1:
		N = T[0].split(" ")
		if len(N) == 1:
			Result += Numbers[N[0]] * 1000
		elif "hundred" not in N:
			Result += (Numbers[N[0]] + Numbers[N[1]]) * 1000
		else:
			N = N[::-1]
			R = 0
			i = 0
			while i < len(N):
				if N[i] in Numbers:
					R += Numbers[N[i]]
				elif N[i] == "hundred":
					h = 100
					e = Numbers[N[i+1]]
					if i+2 < len(N):
						t = Numbers[N[i+2]]
						R += (t+e)*h
						i += 2
					else:
						R += e*h
						i += 1
				i += 1
						
			Result += R * 1000
	
	if len(T) > 1:
		T = T[1:]
	if T[0].startswith(" "):
		T[0] = T[0][1:]
	
	if T == [""]:
		Result = Result
	else:
		T = T[0].split(" ")
		if len(T) == 1:
			Result += Numbers[T[0]]
		elif "hundred" not in T:
			Result += Numbers[T[0]] + Numbers[T[1]]
		else:
			T = T[::-1]
			R = 0
			i = 0
			while i < len(T):
				if T[i] in Numbers:
					R += Numbers[T[i]]
				elif T[i] == "hundred":
					h = 100
					e = Numbers[T[i+1]]
					if i+2 < len(T):
						t = Numbers[T[i+2]]
						R += (t+e)*h
						i += 2
					else:
						R += e*h
						i += 1
				i += 1
			Result += R
	
	if Neg == True:
		Result = Result * (-1)
	print Result
	

#test_cases.close()