data = ['foo@bar.com', 'this is not an email id', 'admin#codeeval.com', 'good123@bad.com', 'A@b@c@example.com', 'b@d.net', 'a"b(c)d,e:f;g<h>i[j\k]l@example.com',
		'"very.unusual.@.unusual.com"@example.com', 'Abc.example.com']


import string
#print string.ascii_lowercase
#print string.ascii_uppercase

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	address = test.rstrip()
	#print address
	if ' ' in address:
		print 'false'
	elif not address.endswith('.com') and not address.endswith('.net'):
		print 'false'
	elif '@' not in address:
		print 'false'
	else:
		idx = address.rfind('@')
		A = address[:idx]
		if (A.startswith('"') and A.endswith('"')):
			print 'true'
		else:
			spec_char = [".", "_", "-", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
			R = ''
			for l in A:
				if ((not l in string.ascii_lowercase) and (l not in string.ascii_uppercase) and (l not in spec_char)):
					R = 'false'
					break
			if R == 'false':
				print 'false'
			else:
				print 'true'

#test_cases.close()