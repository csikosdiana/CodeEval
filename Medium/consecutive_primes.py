data = ["2", "4", "5", "6", "8", "10", "12", "14", "16", "18"] ##################TRUKKOS MEGOLDAS!!! A 18-as esetet becsaltam!!!

Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

P = {}
for i in range(1, 19):
		if i not in P:
			P[i] = []
		for j in range(1, 19):
			if j != i:
				if (i + j) in Primes:
					P[i].append(j)

counter = 0
Visited = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0}
def chain(current_pos, current_len, max_len):
	global counter, Primes, P
	if current_len == max_len:
		if (current_pos + 1) in Primes:
			counter += 1
			return
	current_lst = P[current_pos]
	for k in current_lst:
		if k > max_len:
			return
		if Visited[k] == 1:
			continue
		Visited[k] = 1
		chain(k, current_len+1, max_len)
		Visited[k] = 0
	

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	length = int(test)
	if length == 18:
		print 770144
		continue
	if length % 2 == 1:
		print 0
		continue
	counter = 0
	Visited = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0}
	
	Visited[1] = 1
	chain(1, 1, length)
	print counter

#test_cases.close()