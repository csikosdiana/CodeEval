data = ["Feb 2004-Dec 2009; Sep 2004-Jul 2008",
		"Aug 2013-Mar 2014; Apr 2013-Aug 2013; Jun 2014-Aug 2015; Apr 2003-Nov 2004; Apr 2014-Jan 2015",
		"Mar 2003-Jul 2003; Nov 2003-Jan 2004; Apr 1999-Nov 1999",
		"Apr 1992-Dec 1993; Feb 1996-Sep 1997; Jan 2002-Jun 2002; Sep 2003-Apr 2004; Feb 2010-Nov 2011",
		"Feb 2004-May 2004; Jun 2004-Jul 2004"]

months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06",
			"Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.replace("-", " ")
	test = test.replace(";", "")
	dates = test.split(" ")
	D = []
	for i in dates:
		if i in months:
			i = months[i]
			D.append(i)
		else:
			D.append(i)
	
	i = 0
	Num_dates = []
	while i < len(D) - 1:
		n = int(D[i+1] + D[i])
		Num_dates.append(n)
		i += 2
	
	starts = []
	ends = []
	
	for j in range(0, len(Num_dates)):
		if j % 2 == 0:
			starts.append([Num_dates[j] // 100, Num_dates[j] % 100, 1])
		else:
			if ((Num_dates[j] // 100 % 4 == 0) and (Num_dates[j] % 100 == 2)):
				ends.append([Num_dates[j] // 100, Num_dates[j] % 100, 29])
			elif (Num_dates[j] % 100 == 2):
				ends.append([Num_dates[j] // 100, Num_dates[j] % 100, 28])
			elif (Num_dates[j] % 100 in [4, 6, 9, 11]):
				ends.append([Num_dates[j] // 100, Num_dates[j] % 100, 30])
			else:
				ends.append([Num_dates[j] // 100, Num_dates[j] % 100, 31])

	#print starts
	#print ends
	from datetime import date
	basic = date(1990, 1, 1)
	
	D = []
	
	for w in range(0, len(starts)):
		startdate = date(starts[w][0], starts[w][1], starts[w][2])
		enddate = date(ends[w][0], ends[w][1], ends[w][2])
		R = range((startdate - basic).days, (enddate - basic).days + 1)
		D.append(R)
	SET = []
	for d in range(0, len(D)-1):
		S = list(set(D[d]) | set(D[d+1]))
		SET = list(set(SET) | set(S))
	SET = sorted(SET)
	#print SET
	work = 0
	s = SET[0]
	k = s
	i = 1
	while i < len(SET):
		if SET[i] != (k + 1):
			work = work + (SET[i-1] - (s-1))
			s = SET[i]
			k = s
		else:
			k = k + 1
		i += 1
	work = work + (SET[i-1] - (s-1))
	print work // 365

#test_cases.close()