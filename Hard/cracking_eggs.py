data = ["2 100",
		"2 6",
		"7 30",
		"1 50",
		"6 2500",
		"3 21"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	test = test.split(" ")
	eggs = int(test[0])
	floors = int(test[1])
	if eggs == 1:
		print floors
	else:
		Drops = [1]*floors
		i = 2
		while i <= eggs:
			D = [1]
			for j in range(0, len(Drops)-2):
				D.append(Drops[j] + D[j])
			Drops = D[:]
			i += 1
		count = 1
		for i in range(len(Drops)):
			count += Drops[i]
			if count > floors:
				print i+1
				break
		
#test_cases.close()