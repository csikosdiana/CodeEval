data = ["Vampires: 1, Zombies: 1, Witches: 1, Houses: 1",
		"Vampires: 3, Zombies: 2, Witches: 1, Houses: 10"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.replace(" ", "")
	T = test.split(",")
	#print T
	V = int(T[0].split(":")[1])
	Z = int(T[1].split(":")[1])
	W = int(T[2].split(":")[1])
	H = int(T[3].split(":")[1])
	child = V + Z + W
	print (V*3 + Z*4 + W*5)*H // child

#test_cases.close()