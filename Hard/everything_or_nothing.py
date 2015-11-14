data = ["user_1=>file_1=>read user_2=>file_2=>write",
		"user_1=>file_1=>grant=>read=>user_4 user_4=>file_1=>read",
		"user_4=>file_1=>read",
		"user_2=>file_1=>grant=>read=>user_4"]

def Tb():
	T = [["111", "011", "000"],
		["110", "010", "100"],
		["101", "001", "101"],
		["011", "111", "001"],
		["110", "000", "010"],
		["100", "010", "110"]]
	return T

Users = {"user_1":0, "user_2":1, "user_3":2, "user_4":3, "user_5":4, "user_6":5}
method = {"read":0, "write":1, "grant":2}
Files = {"file_1":0, "file_2":1, "file_3":2}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	Table = Tb()
	Valid = True
	for u in test:
		u = u.split("=>")
		user = Users[u[0]]
		file = Files[u[1]]
		if u[2] == "grant":
			if Table[user][file][2] == "0":
				Valid = False
				break
			m = method[u[3]]
			c = Users[u[4]]
			k = list(Table[c][file])
			k[m] = "1"
			Table[c][file] = "".join(k)
		elif u[2] == "read":
			if Table[user][file][0] == "0":
				Valid = False
				break
		else:
			if Table[user][file][1] == "0":
				Valid = False
				break
	print Valid

#test_cases.close()