data = ["Higher meaning;Hi mean",
		"this is impossible;im possible",
		"twenty   two minutes;two minutes",
		"Higher meaning;e"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(";")
	string1 = " ".join(test[0].split())
	string1 = string1.split(" ")
	string2 = test[1].split(" ")
	#print string1, string2
	Result = []
	s1 = 0
	s2 = 0
	good_id = []
	wrong_id = []
	while s1 <= len(string1)-1:
		if s2 < len(string2):
			if string2[s2] in string1[s1]:
				x = string1[s1]
				l = len(string2[s2])
				idx = x.index(string2[s2])
				Result.append("_"*len(x[:idx]) + string2[s2] + "_"*len(x[(idx+l):]))
				good_id.append(s1)
				s1 += 1
				s2 += 1
			else:
				wrong_id.append(s1)
				s1 += 1
		else:
			if s1 <= len(string1) - 1:
				for i in range(s1, len(string1)):
					wrong_id.append(i)
			break
	#print good_id
	#print wrong_id
	if len(good_id) != len(string2):
		Result = "I cannot fix history"
		print Result
	else:
		R = [""]*len(string1)
		k = 0
		for i in Result:
			R[good_id[k]] = i
			k += 1
		for j in wrong_id:
			R[j] = "_"*len(string1[j])
		Result = R
		print " ".join(Result)

#test_cases.close()
