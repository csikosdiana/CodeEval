def palindrome(n):
	n = str(n)
	rev_n = n[::-1]
	if n == rev_n:
		return True
	return False
	
def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, (n/2)+1):
		if n%i == 0:
			return False
	return True

PP = 0
k = 1000
while PP == 0:
	P = palindrome(k)
	if P == True:
		pr = is_prime(k)
		if pr == True:
			PP = k
	k = k - 1
print PP