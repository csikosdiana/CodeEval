data = ['AD 2H | H',
		'KD KH | C',
		'JH 10S | C']
		
costs = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	if len(test) == 0:
		continue
	test = test.rstrip()
	l = test.split(' | ')
	trump = l[1]
	cards = l[0].split(' ')
	card1_ = cards[0]
	card2_ = cards[1]
	if card1_[0] == '1':
		card1 = 'T' + card1_[-1]
	else:
		card1 = card1_
	
	if card2_[0] == '1':
		card2 = 'T' + card2_[-1]
	else:
		card2 = card2_
	
	if trump == card1[-1] and trump == card2[-1]:
		if card1[0] == card2[0]:
			if card1[0] == 'T':
				card1 = card1_
				card2 = card2_
			print ' '.join([card1, card2])
		elif costs[card1[0]] > costs[card2[0]]:
			if card1[0] == 'T':
				card1 = card1_
			print card1
		else:
			if card2[0] == 'T':
				card2 = card2_
			print card2
	elif trump == card1[-1]:
		if card1[0] == 'T':
			card1 = card1_
		print card1
	elif trump == card2[-1]:
		if card2[0] == 'T':
			card2 = card2_
		print card2
	else:
		if card1[0] == card2[0]:
			if card1[0] == 'T':
				card1 = card1_
				card2 = card2_
			print ' '.join([card1, card2])
		elif costs[card1[0]] > costs[card2[0]]:
			if card1[0] == 'T':
				card1 = card1_
			print card1
		else:
			if card2[0] == 'T':
				card2 = card2_
			print card2
	

#test_cases.close()