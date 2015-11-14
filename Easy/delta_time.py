data = ['14:01:57 12:47:11',
		'13:09:42 22:16:15',
		'08:08:06 08:38:28',
		'23:35:07 02:49:59',
		'14:31:45 14:46:56']
		

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	times = test.split(" ")
	time1 = map(int, times[0].split(":"))
	time2 = map(int, times[1].split(":"))
	T1 = time1[0]*3600 + time1[1]*60 + time1[2]
	T2 = time2[0]*3600 + time2[1]*60 + time2[2]
	delta = abs(T1 - T2)
	H = delta // 3600
	m = (delta % 3600) // 60
	s = ((delta % 3600) % 60)
	Delta_T = []
	if len(str(H)) == 0:
		Delta_T.append('00')
	elif len(str(H)) == 1:
		Delta_T.append('0' + str(H))
	else:
		Delta_T.append(str(H))
	
	if len(str(m)) == 0:
		Delta_T.append('00')
	elif len(str(m)) == 1:
		Delta_T.append('0' + str(m))
	else:
		Delta_T.append(str(m))
	
	if len(str(s)) == 0:
		Delta_T.append('00')
	elif len(str(s)) == 1:
		Delta_T.append('0' + str(s))
	else:
		Delta_T.append(str(s))
	
	print ":".join(Delta_T)

#test_cases.close()