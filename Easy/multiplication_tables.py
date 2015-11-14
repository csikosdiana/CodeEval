i = 1
while i < 13:
	line = ''
	for j in range(1, 13):
		k = str(i*j)
		l = len(k)
		if l == 1:
			line = line + '   ' + k
		elif l == 2:
			line = line + '  ' + k
		else:
			line = line + ' ' + k

	print line
	i += 1