data = ['6D 7H AH 7S QC 6H 2D TD JD AS',
		'JH 5D 7H TC JS JD JC TS 5S 7S',
		'2H 8C AD TH 6H QD KD 9H 6S 6C',
		'JS JH 4H 2C 9H QH KC 9D 4D 3S',
		'TC 7H KH 4H JC 7D 9S 3H QS 7S',
		'8C AS 9D 8D 9C 9S 6H 8H 9H 8S']


def card_values(nums, colors):
	value = 0
	highest = []
	if len(set(colors)) == 1:
		if set([10, 11, 12, 13, 14]) == set(nums):
			value = 10 #Royal Flush
			highest = [14]
		elif set(nums) == set([2, 3, 4, 5, 6]) or set(nums) == set([3, 4, 5, 6, 7]) or set(nums) == set([4, 5, 6, 7, 8]):
			value = 9 #Straight Flush
			highest = [max(nums)]
		elif set(nums) == set([5, 6, 7, 8, 9]) or set(nums) == set([6, 7, 8, 9, 10]) or set(nums) == set([7, 8, 9, 10, 11]):
			value = 9 #Straight Flush
			highest = [max(nums)]
		elif set(nums) == set([8, 9, 10, 11, 12]) or set(nums) == set([9, 10, 11, 12, 13]) or set(nums) == set([10, 11, 12, 13, 14]):
			value = 9 #Straight Flush
			highest = [max(nums)]
		else:
			value = 6 # Flush
			highest = [max(nums)]
	else:
		if len(set(nums)) == 2 and nums.count(list(set(nums))[0]) == 4 and nums.count(list(set(nums))[1]) == 1:
			value = 8 #Four of a Kind
			highest = [list(set(nums))[0]]
		elif len(set(nums)) == 2 and nums.count(list(set(nums))[0]) == 1 and nums.count(list(set(nums))[1]) == 4:
			value = 8 #Four of a Kind
			highest = [list(set(nums))[1]]
		elif len(set(nums)) == 2 and nums.count(list(set(nums))[0]) == 3 and nums.count(list(set(nums))[1]) == 2:
			value = 7 #Full House
			highest = [list(set(nums))[0], list(set(nums))[1]]
		elif len(set(nums)) == 2 and nums.count(list(set(nums))[0]) == 2 and nums.count(list(set(nums))[1]) == 3:
			value = 7 #Full House
			highest = [list(set(nums))[1], list(set(nums))[0]]
		elif set(nums) == set([2, 3, 4, 5, 6]) or set(nums) == set([3, 4, 5, 6, 7]) or set(nums) == set([4, 5, 6, 7, 8]):
			value = 5 #Straight
			highest = [max(nums)]
		elif set(nums) == set([5, 6, 7, 8, 9]) or set(nums) == set([6, 7, 8, 9, 10]) or set(nums) == set([7, 8, 9, 10, 11]):
			value = 5 #Straight
			highest = [max(nums)]
		elif set(nums) == set([8, 9, 10, 11, 12]) or set(nums) == set([9, 10, 11, 12, 13]) or set(nums) == set([10, 11, 12, 13, 14]):
			value = 5 #Straight
			highest = [max(nums)]
		
		elif len(set(nums)) == 3 and nums.count(list(set(nums))[0]) == 3:
			value = 4 #Three of a Kind
			highest = [list(set(nums))[0]]
		elif len(set(nums)) == 3 and nums.count(list(set(nums))[1]) == 3:
			value = 4 #Three of a Kind
			highest = [list(set(nums))[1]]
		elif len(set(nums)) == 3 and nums.count(list(set(nums))[2]) == 3:
			value = 4 #Three of a Kind
			highest = [list(set(nums))[2]]
		
		elif len(set(nums)) == 3 and nums.count(list(set(nums))[0]) == 2 and nums.count(list(set(nums))[1]) == 2:
			value = 3 #Two Pairs
			ma = max([list(set(nums))[0], list(set(nums))[1]])
			mi = min([list(set(nums))[0], list(set(nums))[1]])
			highest = [ma, mi]
		elif len(set(nums)) == 3 and nums.count(list(set(nums))[0]) == 2 and nums.count(list(set(nums))[2]) == 2:
			value = 3 #Two Pairs
			ma = max([list(set(nums))[0], list(set(nums))[2]])
			mi = min([list(set(nums))[0], list(set(nums))[2]])
			highest = [ma, mi]
		elif len(set(nums)) == 3 and nums.count(list(set(nums))[1]) == 2 and nums.count(list(set(nums))[2]) == 2:
			value = 3 #Two Pairs
			ma = max([list(set(nums))[1], list(set(nums))[2]])
			mi = min([list(set(nums))[1], list(set(nums))[2]])
			highest = [ma, mi]
		
		elif len(set(nums)) == 4:
			value = 2 #One Pair
			for n in nums:
				if nums.count(n) == 2:
					highest = [n]
					break
		

	return [value, highest]


values = {"T":"10", "J":"11", "Q":"12", "K":"13", "A":"14"}

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	T = test.split(' ')
	left_player = T[:5]
	l_nums = []
	l_colors = []
	right_player = T[5:]
	r_nums = []
	r_colors = []
	for i in range(5):
		if left_player[i][0] in values:
			l_nums.append(values[left_player[i][0]])
		else:
			l_nums.append(left_player[i][0])
		
		l_colors.append(left_player[i][1])
		
		if right_player[i][0] in values:
			r_nums.append(values[right_player[i][0]])
		else:
			r_nums.append(right_player[i][0])
			
		r_colors.append(right_player[i][1])
		
	l_nums = map(int, l_nums)
	r_nums = map(int, r_nums)
	[left_point, left_highest] = card_values(l_nums, l_colors)
	[right_point, right_highest] = card_values(r_nums, r_colors)
	#print left_point, left_highest
	#print right_point, right_highest

	if left_point > right_point:
		print "left"
	elif right_point > left_point:
		print "right"
	else:
		if left_point == 0:
			print "none"
		elif left_highest[0] > right_highest[0]:
			print "left"
		elif right_highest[0] > left_highest[0]:
			print "right"
		else:
			if len(left_highest) > 1:
				if left_highest[1] > right_highest[1]:
					print "left"
				elif right_highest[1] > left_highest[1]:
					print "right"
				else:
					L = max([i for i in l_nums if i != left_highest[0] and i != left_highest[1]])
					R = max([i for i in r_nums if i != right_highest[0] and i != right_highest[1]])
					if L > R:
						print "left"
					elif R > L:
						print "right"
					else:
						print "none"
			else:
				L = max([i for i in l_nums if i != left_highest[0]])
				R = max([i for i in r_nums if i != right_highest[0]])
				if L > R:
					print "left"
				elif R > L:
					print "right"
				else:
					print "none"
	

#test_cases.close()