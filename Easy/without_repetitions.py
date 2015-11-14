data = ["But as he spake he drew the good sword from its scabbard, and smote a heathen knight, Jusssstin of thee Iron Valley.",
		"No matttter whom you choose, she deccccclared, I will abide by your decision.",
		"Wwwhat is your will?",
		"At his magic speech the ground oppened and he began the path of descent.",
		"I should fly away and you would never see me again."]
		
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	w_r = test[0]
	for l in test[1:]:
		if l != w_r[len(w_r) - 1]:
			w_r = w_r + l
	print w_r
#test_cases.close()