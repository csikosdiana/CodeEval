def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, (n/2)+1):
		if n%i == 0:
			return False
	return True

count = 0
p = 2
SUM = 0
while count < 1000:
	if is_prime(p) == True:
		SUM = SUM + p
		count = count + 1
	p = p + 1
	
print SUM