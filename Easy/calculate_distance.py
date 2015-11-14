data = ['(25, 4) (1, -6)', '(47, 43) (-25, -11)']

import math
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	chars_to_remove = ['(', ')', ',']
	test = test.translate(None, ','.join(chars_to_remove))
	test = test.split(" ")
	numbers = map(int, test)
	distance = math.sqrt((numbers[0] - numbers[2])**2 + (numbers[1] - numbers[3])**2)
	print int(distance)

#test_cases.close()