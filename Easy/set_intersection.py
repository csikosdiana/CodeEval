data = ['59,60,61,62,63,64,65,66,67,68,69;75,76,77,78,79,80,81,82,83,84,85,86,87,88,89', '20,21,22;45,46,47', '7,8,9;8,9,10,11,12', '70,71,72,73,74;59,60,61,62,63,64,65,66,67,68,69,70,71']

data1 = ['9,10,11;33,34,35', '7,8,9;8,9,10,11,12']
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.split(";")
	A = num[0].split(",")
	B = num[1].split(",")
	A = map(int, A)
	B = map(int, B)
	I = list(set(A) & set(B))
	I = map(str, I)
	print ",".join(I)

#test_cases.close()

