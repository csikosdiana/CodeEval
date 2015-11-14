input = 'c b m u x y q f s t l o a z w i 9'
l = input.split()
k = l.pop()
if len(l) >= int(k):
	print l[::-1][int(k)-1]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
#for test in data:
#    l = test.split()
#    k = l.pop()
#	if len(l) >= int(k):
#	print l[::-1][int(k)-1]