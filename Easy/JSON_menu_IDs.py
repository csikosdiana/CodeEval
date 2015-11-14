data = ['{"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85}, {"id": 54}, null, {"id": 46, "label": "Label 46"}]}}',
		'{"menu": {"header": "menu", "items": [{"id": 81}]}}',
		'{"menu": {"header": "menu", "items": [{"id": 70, "label": "Label 70"}, {"id": 85, "label": "Label 85"}, {"id": 93, "label": "Label 93"}, {"id": 2}]}}']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	J_string = test.replace("}", "{")
	J_string = J_string.split("{")
	ID_sum = 0
	J = []
	for j in J_string:
		if '"label"' in j:
			J.append(j)
			k = j.split('"id": ',1)[1]
			k = k.split(",")
			n = int(k[0])
			ID_sum = ID_sum + n
	print ID_sum
	

#test_cases.close()