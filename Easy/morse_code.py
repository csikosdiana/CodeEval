data = ['.- ...- ..--- .-- .... .. . -.-. -..-  ....- .....', '-... .... ...--']

CODE_1 = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
		'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
		'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
		'8': '---..', '9': '----.'}
CODE_2 = dict()
for k, v in CODE_1.items():
	CODE_2[v] = k


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split("  ")
	Decoded = []
	for i in test:
		letters = i.split(" ")
		Word = ''
		for l in letters:
			Word = Word + CODE_2[l]
		Decoded.append(Word)
	print " ".join(Decoded)
	

#test_cases.close()