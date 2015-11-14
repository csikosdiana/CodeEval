data = ["-1 -4 -5 -4",
		"-5 8 -1 3",
		"-2 1 3 2",
		"1 5 6 -9"]

def Kadane(lst):
	current_sum = lst[0]
	Max_sum = lst[0]
	for i in range(1, len(lst)):
		current_sum = max(lst[i], lst[i] + current_sum)
		Max_sum = max(current_sum, Max_sum)
	return Max_sum


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
Matrix = []
for test in data:
	test = test.rstrip()
	row = test.split(" ")
	row = map(int, row)
	if Matrix == []:
		for r in row:
			Matrix.append([r])
	else:
		for i in range(len(row)):
			Matrix[i].append(row[i])

#test_cases.close()

MAX_SUM = -1000000
#print Matrix
l = len(Matrix[0])
L = 0
while L < len(Matrix):
	S = [0] * l
	for R in range(L, l):
		if S == [0] * l:
			S = Matrix[R]
			Curr_sum = Kadane(S)
			if Curr_sum > MAX_SUM:
				MAX_SUM = Curr_sum
		else:
			S = [S[i] + Matrix[R][i] for i in range(len(S))]
			Curr_sum = Kadane(S)
			if Curr_sum > MAX_SUM:
				MAX_SUM = Curr_sum
	L += 1

print MAX_SUM	