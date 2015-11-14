data = ['Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;', 'Vgdfz,70; Mgknxpi,3958; Nsptghk,2626; Wuzp,2559; Jcdwi,3761;',
		'Yvnzjwk,5363; Pkabj,5999; Xznvb,3584; Jfksvx,1240; Inwm,5720;', 'Ramytdb,2683; Voclqmb,5236;']

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	road = test.split(";")
	road.pop()
	trip = []
	for r in road:
		r = r.split(",")
		trip.append(int(r[1]))
	trip = sorted(trip)
	dist = [trip[0]]
	i = 1
	while i < len(trip):
		d = trip[i] - trip[i-1]
		dist.append(d)
		i = i + 1
	dist = map(str, dist)
	print ",".join(dist)
	

#test_cases.close()