data = ["1 2",
		"1 7",
		"87 88"]

def is_palindromic(n):
	n = str(n)
	if n == n[::-1]:
		return True
	else:
		return False
		
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	ranges = test.split(" ")
	L = int(ranges[0])
	R = int(ranges[1])
	#print L, R
	interesting_ranges = 0
	for i in range(L, R+1):
		for j in range(i, R+1):
			count = 0
			for k in range(i, j+1):
				p = is_palindromic(k)
				if p:
					count += 1
			#print count
			if count % 2 == 0:
				interesting_ranges += 1
	print interesting_ranges

#test_cases.close()