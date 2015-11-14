data = ["rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcp",
		"tc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"de kr kd eoya kw aej icfkici re zjkr"]
import string
L1 = string.ascii_lowercase
L2 = string.ascii_lowercase

coded = "rbc vjnmkf kd yxyqci na rbc zjkfoscdd ew rbc ujllmcp tc rbkso rbyr ejp mysljylc kd kxveddknmc re jsicpdrysi de kr kd eoya kw aej icfkici re zjkr"
decoded = "the public is amazed by the quickness of the juggler we think that our language is impossible to understand so it is okay if you decided to quit"

decoder = {"n":"b", "u":"j", "g":"v"}
for i in range(len(coded)):
	decoder[coded[i]] = decoded[i]
	L1 = L1.replace(coded[i], "")
	L2 = L2.replace(decoded[i], "")
for j in range(len(L1)):
	if L1[j] not in decoder:
		decoder[L1[j]] = L2[j]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	if test:
		coded_text = test.rstrip()
		decoded_text = ""
		for l in coded_text:
			decoded_text = decoded_text + decoder[l]
		print decoded_text
	
	
#test_cases.close()