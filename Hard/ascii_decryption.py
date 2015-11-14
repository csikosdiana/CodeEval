data = ["5 | s | 92 112 109 40 118 109 109 108 123 40 119 110 40 124 112 109 40 117 105 118 129 40 119 125 124 127 109 113 111 112 40 124 112 109 40 118 109 109 108 123 40 119 110 40 124 112 109 40 110 109 127 54 40 53 40 91 120 119 107 115",
		"9 | r | 101 119 116 107 113 119 117 103 116 34 99 112 102 34 101 119 116 107 113 119 117 103 116 35 47 34 78 103 121 107 117 34 69 99 116 116 113 110 110 46 34 67 110 107 101 103 34 107 112 34 89 113 112 102 103 116 110 99 112 102"]

import string
S = sorted(string.printable)
L = string.ascii_letters

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	length = int(test[0])
	last_char = test[1]
	coded_text = test[2].split(" ")
	coded_text = map(int, coded_text)
	#print length
	#print last_char
	#print coded_text
	k = 0
	rep_word = ""
	R = []
	while k < len(coded_text) - length:
		T1 = coded_text[k:(k+length)]
		for j in range(k+length, len(coded_text)):
			T2 = coded_text[j:(j+length)]
			if T2 == T1:
				R.append(T2)
				if coded_text[j-1] == coded_text[j+length]:
					rep_word = coded_text[j:(j+length)]
					break

		k += 1
		if rep_word != "":
			break
	if rep_word == "":
		if R != []:
			rep_word = R[0]

	#print rep_word
	id = S.index(last_char)
	key = rep_word[-1] - id
	#print key
	decoded_text = []
	for i in coded_text:
		t = i - key
		#print t
		decoded_text.append(S[t])
	print "".join(decoded_text)
	
	

#test_cases.close()