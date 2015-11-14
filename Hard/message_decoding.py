data = ["$#**\\0100000101101100011100101000"]

Bin = {"001":1, "010":2, "011":3, "100":4, "101":5,"110":6}

import itertools
Decoder = ["0"]
for i in range(2, 7):
	T = list(itertools.product('01', repeat=i))
	for t in T:
		t = "".join(list(t))
		if "0" in t:
			Decoder.append(t)

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	i1 = test.index("0")
	i2 = test.index("1")
	m = min(i1, i2)
	alphabet = test[:m]
	code = test[m:]
	new = False
	i = 0
	j = 3
	Message = []
	while j < len(code):
		length = code[i:j]
		if length == "000":
			break
		k = Bin[length]
		while True:
			l = code[j:(j+k)]
			if l == "1"*k:
				i = j + k
				j = i + 3
				break
			else:
				Message.append(l)
			j = j + k
	#print Message
	l1 = len(alphabet)
	D = Decoder[:l1]
	Decoded_Message = ""
	for m in Message:
		idx = D.index(m)
		letter = alphabet[idx]
		Decoded_Message += letter
	print Decoded_Message
	

#test_cases.close()