data = ["10110001 11111000 11111110 11111111 11111111 11111111 11111111 11101101 11111111 01111111 11110010 10100111;84.525784",
		"11111111 11110110 11101111 11110111 10111110 11110110 10111011 10100111 11111100 01100100 11111101 01011110;5.57",
		"11000010 00001111 11111111 10111111 11101011 11110011 01111110 11011111 11111111 11111111 11111001 01101110;857.71284",
		"11111111 01110111 10111011 11001101 11111011 11101010 11110100 01001101 11011111 11111010 10010110 10111111;66.92",
		"11111011 10010001 11111011 11111101 10011111 10111110 01111100 11011101 10111001 11111110 11101111 11110110;188.87",
		"11111111 01110111 10111011 11001101 11111011 11101010 11110100 01001101 11011111 11111010 10010110 10111111;662.",
		"10111111 10110110 10011011 01111011 11110011 11111101 11111110 11111111 11111111 11111111 11110001 11011111;726.681"]

N = {"0":"1111110", "1":"0110000", "2":"1101101", "3":"1111001", "4":"0110011", "5":"1011011", "6":"1011111",
		"7":"1110000", "8":"1111111", "9":"1111011"}

def displayable(where, what):
	if where == "11111111":
		return True
	else:
		for i in range(len(what)):
			if what[i] == "1" and where[i] != "1":
				return False
			else:
				continue
	return True


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(";")
	lcd = test[0].split(" ")
	num = test[1]
	#print num
	dot = num.index(".") - 1
	num = num.replace(".", "")
	disp_num = []
	for i in range(len(num)):
		if i == dot:
			disp_num.append(N[num[i]] + "1")
		else:
			disp_num.append(N[num[i]] + "0")
	#print disp_num
	count = 0
	k = 0
	for i in lcd:
		if displayable(i, disp_num[k]) == True:
			count += 1
			k += 1
		else:
			continue
		if k == len(disp_num):
			break
	if count == len(disp_num):
		print 1
	else:
		print 0


#test_cases.close()