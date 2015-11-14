data = ['SetCol 32 20',
		'SetRow 15 7',
		'SetRow 16 31',
		'QueryCol 32',
		'SetCol 2 14',
		'QueryRow 10',
		'SetCol 14 0',
		'QueryRow 15',
		'SetRow 10 1',
		'QueryCol 2']

A = [[0]*256] * 256

def SetCol(A, n, m):
	for i in A:
		i[n] = m
	return A
def SetRow(A, n, m):
	l = len(A[n])
	A[n] = [m]* l
	return A

def QueryCol(A, n):
	SUM = 0
	for i in A:
		SUM = SUM + i[n]
	return SUM
	
def QueryRow(A, n):
	return sum(A[n])

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	if test[0] == 'SetCol':
		A = SetCol(A, int(test[1]), int(test[2]))
	elif test[0] == 'SetRow':
		A = SetRow(A, int(test[1]), int(test[2]))
	elif test[0] == 'QueryCol':
		print QueryCol(A, int(test[1]))
	elif test[0] == 'QueryRow':
		print QueryRow(A, int(test[1]))


#test_cases.close()