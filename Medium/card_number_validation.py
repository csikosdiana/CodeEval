data = ["1556 9144 6285 339",
		"6011 5940 0319 9511",
		"5537 0213 6797 6815",
		"5574 8363 8022 9735",
		"3044 8507 9391 30",
		"6370 1675 9034 6211 774"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.replace(" ", "")
	card = map(int, list(test))[::-1]
	new_card = []
	for i in range(0, len(card)):
		if i % 2 == 1:
			c = 2*card[i]
			if c > 9:
				c = c // 10 + c % 10
		
			new_card.append(c)
		else:
			new_card.append(card[i])
	if sum(new_card) % 10 == 0:
		print 1
	else:
		print 0
	
	

#test_cases.close()