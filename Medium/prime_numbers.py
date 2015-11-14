data = ['10', '20', '100']

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, (n/2)+1):
		if n%i == 0:
			return False
	return True

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	primes = []
	N = range(2, int(test))
	for i in range(0, len(N)):
		if N[i] == 0:
			continue
		else:
			p = is_prime(N[i])
			if p == True:
				primes.append(str(N[i]))
				k = N[i]
				j = i
				for n in range(j, len(N), k):
					N[n] = 0
	
	print ",".join(primes)

#test_cases.close()