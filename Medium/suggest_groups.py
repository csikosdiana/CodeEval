data = ["Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral collecting",
		"Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral collecting",
		"Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling",
		"Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby",
		"Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting,Rugby",
		"Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting",
		"Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting",
		"Un:Amira,Margarito,Wilford:",
		"Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling,Mineral collecting",
		"Wilford:Isaura,Shakira,Un:Driving"]

users_groups = {}
users = []
friends = {}
Groups = {}
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(":")
	users.append(test[0])
	users_groups[test[0]] = test[2].split(",")
	T = test[1].split(",")
	if test[0] not in friends:
		friends[test[0]] = T
		for f in T:
			if f not in friends:
				friends[f] = [test[0]]
			else:
				if test[0] not in friends[f]:
					friends[f].append(test[0])
	else:
		for f in T:
			if f not in friends[test[0]]:
				friends[test[0]].append(f)
	G = test[2].split(",")
	for g in G:
		if g not in Groups and g != "":
			Groups[g] = 0

#test_cases.close()

#print users_groups
#print friends
#print Groups
#print users

for i in users:
	F = friends[i]
	l = len(F)
	#print i, l
	Suggested = []
	limit = int(round(l / float(2)))
	count_group = dict(Groups)
	for j in F:
		gr = users_groups[j]
		if gr != [""]:
			for k in gr:
				count_group[k] += 1
				if count_group[k] >= limit and k not in Suggested:
					if k not in users_groups[i]:
						Suggested.append(k)
	#print count_group
	#print Suggested
	
	if Suggested != []:
		Suggested = sorted(Suggested)
		#print Suggested
		print i + ":" + ",".join(Suggested)
