data = ["Lorem ipsum dolor sit amet. Mea et habeo doming praesent. Te inani utroque recteque has, sea ne fugit verterem!",
		"Usu ei scripta phaedrum, an sed salutatus definiebas? Qui ut recteque gloriatur reformidans. Qui solum aeque sapientem cu.",
		"Eu nam nusquam quaestio principes."]

slang = [", yeah!", ", this is crazy, I tell ya.", ", can U believe this?", ", eh?",
		", aw yea.", ", yo.", "? No way!", ". Awesome!"]
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
position = 0
s = 0
for test in data:
	test = test.rstrip()
	text = ""
	for i in test:
		if s == len(slang):
			s = 0

		if ((i == ".") or (i == "!") or (i == "?")):
			position += 1
			if position % 2 == 0:
				t = slang[s]
				s += 1
				text = text + t
			else:
				text = text + i
		else:
			text = text + i
	print text

#test_cases.close()
