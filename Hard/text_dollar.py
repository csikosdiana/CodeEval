data = ["3", "10", "21", "466", "1234", "125000125", "125637", "254019514", "536700613"]

Numbers = {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine",
			"10":"Ten", "11":"Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", "16":"Sixteen", "17":"Seventeen",
			"18":"Eighteen", "19":"Nineteen", "20":"Twenty", "30":"Thirty", "40":"Forty", "50":"Fifty", "60":"Sixty", "70":"Seventy", "80":"Eighty", "90":"Ninety"}

def hundreds(n):
	x = int(n)
	if x == 0:
		return ""
	if x < 20:
		if n[0] == "0":
			n = n[1:]
		return Numbers[n]
	elif x < 100:
		if n[0] == "0":
			n = n[1:]
		t = n[0] + "0"
		e = n[1]
		if e != "0":
			return Numbers[t] + Numbers[e]
		else:
			return Numbers[t]
	else:
		h = n[0]
		if n[1:] in Numbers:
			return Numbers[h] + "Hundred" + Numbers[n[1:]]
		t = n[1]
		e = n[2]
		if t != "0" and e != "0":
			return Numbers[h] + "Hundred" + Numbers[t + "0"] + Numbers[e]
		elif t != "0":
			return Numbers[h] + "Hundred" + Numbers[t + "0"]
		elif e != "0":
			return Numbers[h] + "Hundred" + Numbers[e]
		else:
			return Numbers[h] + "Hundred"

print hundreds("000")

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	num = test.strip("\n")
	Dollars = "Dollars"
	if len(num) <= 3:
		Dollars = hundreds(num) + Dollars
	elif len(num) <= 6:
		T = num[:-3]
		E = num[-3:]
		Dollars = hundreds(T) + "Thousand" + hundreds(E) + Dollars
	elif len(num) <= 9:
		M = num[-9:-6]
		T = num[-6:-3]
		E = num[-3:]
		if hundreds(T) != "":
			Dollars = hundreds(M) + "Million" + hundreds(T) + "Thousand" + hundreds(E) + Dollars
		else:
			Dollars = hundreds(M) + "Million" + hundreds(E) + Dollars
	print Dollars

#test_cases.close()