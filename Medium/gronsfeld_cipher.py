data = ["31415;HYEMYDUMPS",
		'45162;M%muxi%dncpqftiix"',
		"14586214;Uix!&kotvx3"]

decoder = " !\"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip('\n')
	if len(test) == 0:
		continue
	test = test.split(";")
	code = map(int, list(test[0]))
	coded_text = test[1]
	decoded_text = ""
	i = 0
	for k in coded_text:
		h = decoder.index(k) - code[i]
		if h < 0:
			h = h + len(decoder)
		decoded_text = decoded_text + decoder[h]
		i += 1
		if i == len(code):
			i = 0
	print decoded_text

#test_cases.close()