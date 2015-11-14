data = ["3.1415926", "1.41421356", "01-01-1970", "2.7182818284", "4 8 15 16 23 42"]

big_digits = ["-**----*--***--***---*---****--**--****--**---**--",
			"*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-",
			"*--*---*---**---**--****-***--***----*---**---***-",
			"*--*---*--*-------*----*----*-*--*--*---*--*----*-",
			"-**---***-****-***-----*-***---**---*----**---**--",
			"--------------------------------------------------"]
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = list(test)
	i = 0
	while i < 6:
		line = ''
		for n in test:
			try:
				n = int(n)
				if n == 0:
					l = big_digits[i][:5]
				else:
					l = big_digits[i][(n*5):(n*5 + 5)]
					
				line = line + l
			except:
				continue
		print line
		i += 1

#test_cases.close()
