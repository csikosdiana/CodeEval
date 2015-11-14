data = ['2', 'Hello World', 'CodeEval', 'Quick Fox', 'A', 'San Francisco']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
lines = []
for test in data:
	test = test.rstrip()
	lines.append(test)

line_num = int(lines[0])
lines = lines[1:]
lengths = []
for i in lines:
	l = len(i)
	lengths.append(l)

i = 0
while i < line_num:
	idx = lengths.index(max(lengths))
	print lines[idx]
	lines.remove(lines[idx])
	lengths.remove(lengths[idx])
	i = i + 1
#test_cases.close()