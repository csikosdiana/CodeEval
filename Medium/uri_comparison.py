data = ["http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html"]

from urlparse import urlparse
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	urls = test.split(";")
	url1 = urlparse(urls[0])
	url2 = urlparse(urls[1])
	same = True
	
	#SCHEME
	if url1.scheme.lower() != url2.scheme.lower():
		same = False
	
	#NETLOC
	u1 = url1.netloc.lower()
	u2 = url2.netloc.lower()
	if url1.port == 80:
		u1 = u1[:-3]
		if ((url2.port == 80) or (url2.port == None)):
			same = True
		else:
			same = False

	if url2.port == 80:
		u2 = u2[:-3]
		if ((url1.port == 80) or (url1.port == None)):
			same = True
		else:
			same = False
	
	if u1 != u2:
		same = False
	
	#PATH
	from urllib import unquote
	
	p1 = url1.path
	p2 = url2.path
	if unquote(p1) != unquote(p2):
		same = False
	
	print same

#test_cases.close()
