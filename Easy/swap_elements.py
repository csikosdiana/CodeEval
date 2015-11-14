data = ['1 2 3 4 5 6 7 8 9 : 0-8', '1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	H = test.split(" : ")
	numbers = H[0].split(" ")
	swaps = H[1].replace("-" , ",")
	swaps = swaps.split(",")
	i = 0
	while i < len(swaps)-1:
		j = numbers[int(swaps[i])]
		numbers[int(swaps[i])] = numbers[int(swaps[i+1])]
		numbers[int(swaps[i+1])] = j
		i = i + 2
	print " ".join(numbers)

#test_cases.close()