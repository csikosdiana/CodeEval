data = ['cat dog hello', 'stop football play', 'music is my life']


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	l = test.split(" ")
	longest = ''
	max_len = 0
	for i in l:
		length = len(i)
		if length > max_len:
			max_len = length
			longest = i
	stepwise = [longest[0]]
	i = 1
	while i < len(longest):
		stepwise.append('*'*i + longest[i])
		i += 1
	print " ".join(stepwise)

#test_cases.close()