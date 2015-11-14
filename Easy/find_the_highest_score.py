data = ['72 64 150 | 100 18 33 | 13 250 -6',
		'10 25 -30 44 | 5 16 70 8 | 13 1 31 12',
		'100 6 300 20 10 | 5 200 6 9 500 | 1 10 3 400 143',
		'-341 762 592 -50 664 837 | -823 273 863 368 -14 -191 | -555 -677 -441 -656 -86 -47']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	table = test.split(" | ")
	rows = [map(int, i.split(" ")) for i in table]
	l = len(rows[0])
	k = 0
	ColMax = []
	Maxi = -1000
	while k < l:
		for j in rows:
			m = j[k]
			if m > Maxi:
				Maxi = m
		ColMax.append(str(Maxi))
		Maxi = -1000
		k += 1

	print " ".join(ColMax)

#test_cases.close()