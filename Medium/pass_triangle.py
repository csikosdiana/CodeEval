data = ["5", "9 6", "4 6 8", "0 7 1 5"]


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
S = []
for test in data:
	test = test.rstrip()
	nums = test.split(" ")
	nums = map(int, nums)
	if S == []:
		S = nums
		continue
	else:
		T = nums
		E = []
		for i in range(0, len(T)):
			if i == 0:
				E.append((T[i] + S[i]))
			elif i == len(T) - 1:
				E.append((T[i] + S[len(S)-1]))
			else:
				m = max(S[i-1], S[i])
				E.append((T[i] + m))
		S = E

print max(S)
#test_cases.close()
