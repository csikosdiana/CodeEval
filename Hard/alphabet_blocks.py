data = ["4 | DOG | UPZRHR INOYLC KXDHNQ BAGMZI",
		"6 | HAPPY | PKMFQP KTXGCV OSDMAJ SDSIMY OEPGLE JZCDHI",
		"5 | PLAIN | BFUBZD XMQBNM IDXVCN JCOIAM OZYAYH",
		"17 | JKFTWNVZNP | MFIUKE ETEQVT MLXXQH CRTDLX KXBMSC UMJKMD CYAKKI IOUFKV QDIZAK EBYNIH CZCOWS HSTGUW KCNNDT NYYHGG SEBNFO XACPEI RYDANO",
		"17 | AUASJHDCTCW | KBFVSY KJICPW YDMZMG HRDWVP EYPBVS LQYLGC VVYZPB HPJVWD ETXTJH YNFXOW WFYKBQ YELWZU YGDSNP ULQXMM KQKZXH MABVET IIPCUE"]

Visited = []
word = ""
letters = {}
def word_check(pos, current_len, max_len):
	global letters, word, Visited
	if current_len == max_len:
		for p in letters[word[pos]]:
			if p not in Visited:
				return True
		return False
	pos_list = letters[word[pos]]
	for i in pos_list:
		if i in Visited:
			continue
		Visited.append(i)
		Z = word_check(pos + 1, current_len + 1, max_len)
		if Z == True:
			return True
		Visited.pop()
	return False

			
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	test = test.split(" | ")
	N = int(test[0])
	word = test[1]
	blocks = test[2].split(" ")
	letters = {}
	Valid = ""
	for l in word:
		letters[l] = []
		for j in range(N):
			if l in blocks[j]:
				letters[l].append(j)
		if letters[l] == []:
			Valid = False
			break
	if Valid != "":
		print Valid
		continue
	Visited = []
	
	#print letters
	#print word
	print word_check(0, 1, len(word))
	

#test_cases.close()
