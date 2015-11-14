data = ["4155230"]

buttons = {"0":["0"], "1":["1"], "2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"],
			"6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.strip("\n")
	words = []
	for i0 in buttons[num[0]]:
		for i1 in buttons[num[1]]:
			for i2 in buttons[num[2]]:
				for i3 in buttons[num[3]]:
					for i4 in buttons[num[4]]:
						for i5 in buttons[num[5]]:
							for i6 in buttons[num[6]]:
								w = i0 + i1 + i2 + i3 + i4 + i5 + i6
								words.append(w)
	print ",".join(sorted(words))
	

#test_cases.close()