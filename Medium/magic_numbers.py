data = ["10 100", "8382 8841"]

def is_magic_num(n):
	n = list(str(n))
	if len(set(n)) != len(n):
		return False
	else:
		n = map(int,n)
		new_n = [""]*len(n)
		positions = []
		pos = 0
		while pos not in positions:
			positions.append(pos)
			v = (pos + n[pos]) % len(n)
			new_n[v] = n[pos]
			pos = v
		if "" in new_n:
			return False
		if len(set(new_n)) == len(n):
			return True


#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	interval = test.split(" ")
	start = int(interval[0])
	end = int(interval[1])
	magic_numbers = []
	for i in range(start, end+1):
		m = is_magic_num(i)
		if m == True:
			magic_numbers.append(i)
	if magic_numbers == []:
		print -1
	else:
		magic_numbers = map(str, magic_numbers)
		print " ".join(magic_numbers)
	
	

#test_cases.close()