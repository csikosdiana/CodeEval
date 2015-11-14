data = ["22 2 2 9 11", "33 5 0", "16 3 2 6 10", "835 125 1 113", "47 5 0"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	wire = int(test[0])
	dist = int(test[1])
	n = int(test[2])
	bats = []
	count = 0
	if n != 0:
		bats = map(int, test[3:])
		i = 0
		while i < len(bats)-1:
			b = bats[i]
			while b < bats[i+1]:
				b = b + dist
				if (bats[i+1] - b) >= dist:
					count += 1
				else:
					continue
			i += 1
		s = bats[0]
		while s >= 6:
			b = s - dist
			if b >= 6:
				count += 1
			s = b
		e = bats[-1]
		while e <= (wire - 6):
			b = e + dist
			if b <= (wire - 6):
				count += 1
			e = b
	else:
		count = (wire - 12) // (dist - 1)

	print count

#test_cases.close()