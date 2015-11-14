data = ['159', '296', '3992']

Code = {1:"I", 4:"IV", 5:"V", 6:"VI", 9:"IX", 10:"X", 40:"XL", 50:"L", 60:"LX", 90:"XC", 100:"C", 400:"CD", 500:"D", 600:"DC", 900:"CM", 1000:"M"}

NUMS = [1000, 900, 600, 500, 400, 100, 90, 60, 50, 40, 10, 9, 6, 5, 4, 1]
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	arabic = int(test)
	roman = ''
	while arabic > 0:
		for n in NUMS:
			if n <= arabic:
				k = n
				break
		arabic = arabic - k
		roman = roman + Code[k]
	print roman

#test_cases.close()