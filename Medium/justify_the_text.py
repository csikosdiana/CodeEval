data = ["Hello, World!", "The precise 50-digits value of Pi is 3.14159265358979323846264338327950288419716939937510.",
		"But he who would be a great man ought to regard, not himself or his interests, but what is just, whether the just act be his own or that of another. Next as to habitations. Such is the tradition."]

#Hello, World!
#The         precise         50-digits        value        of        Pi        is
#3.14159265358979323846264338327950288419716939937510.
#But  he  who would be a great man ought to regard, not himself or his interests,
#but what is just, whether the just act be his own or that of another. Next as to
#habitations. Such is the tradition.

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	if len(test) <= 80:
		print test
	else:
		words = test.split(" ")
		while len(words) > 0:
			length = 0
			for w in range(len(words)):
				l = len(words[w])
				length = length + l
				if length > 80:
					id = w
					length = length - l - 1
					break
				else:
					id = len(words)
				length += 1
			if id != len(words):
				rest = 80 - length
				r1 = rest // (len(words[:id]) - 1)
				r2 = rest % (len(words[:id])- 1)
		
				line = ""
				for i in range(0, id):
					if i in range(r2):
						s = " "*(r1+1)
						line = line + words[i] + s + " "
					else:
						s = " "*r1
						line = line + words[i] + s + " "
				line = line[:-1]
				print line
			else:
				print " ".join(words)
		
			words = words[id:]

#test_cases.close()