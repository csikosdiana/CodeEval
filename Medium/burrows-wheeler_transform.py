data = ["yyeep$-aass|",
		"oooooooo$  ffffffff     ffffffffuuuuuuuuaaaaaaaallllllllbbBbbBBb|",
		"edarddddddddddntensr$  ehhhhhhhhhhhJ aeaaaaaaaaaaalhtf thmbfe           tcwohiahoJ eeec t e |",
		"ooooio,io$Nnssshhhjo  ee  o  nnkkkkkkii |"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	string = test[:-1]
	sort = sorted(string)
	table1 = {}
	for i in range(0, len(string)):
		char = string[i]
		count = string[:i].count(char)
		table1[i] = count
	#print table1
	table2 = {}
	for i in string:
		if i not in table2:
			idx = sort.index(i)
			l = len(sort[:idx])
			table2[i] = l
	#print table2
	
	S = "$"
	v = string.index("$")
	k = table1[v] + table2["$"]
	l = len(string) - 1
	S = string[k] + S
	curr_char = string[k]
	while l > 1:
		k = table1[k] + table2[curr_char]
		curr_char = string[k]
		S = string[k] + S
		l -= 1
	print S

#test_cases.close()