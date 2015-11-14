data = ["1.029 115 1.122 125 1.185 100 0.53 110 0.751 95 1.242 85 0.533 85 1.003 120 0.465 110 0.546 125 0.446 90 0.582 70 0.878 45 0.49 30 1.016 130 1.047 140 1.146 75 0.496 85 0.857 125 0.971 0",
		"1 266 8.1 1.4",
		"2 178 8.7 4.8",
		"3 251 8.0 3.4",
		"4 215 6.8 3.8",
		"5 220 5.9 3.3",
		"6 262 4.5 1.5",
		"7 267 5.4 2.6",
		"8 268 7.8 3.8",
		"9 225 4.7 1.8",
		"10 266 4.0 1.9"]

#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
route = []
cars = []
for test in data:
	test = test.rstrip()
	test = test.split(" ")
	test = map(float, test)
	if route == []:
		route = test
	else:
		cars.append(test)

#test_cases.close()

car_times = {}
for i in range(len(cars)):
	car = cars[i]
	car_num = int(car[0])
	topspeed, t_ac, t_dec = car[1], car[2] / 3600, car[3] / 3600
	#print topspeed, t_ac, t_dec
	
	ac = topspeed / t_ac
	dec = topspeed / t_dec
	
	TIME = 0
	SPEED = 0
	
	j = 0
	while j < len(route):
		l = route[j]
		a = route[j+1]
		
		t_ac = (topspeed - SPEED) / ac
		dist_to_ac = (SPEED * t_ac) + (0.5 * ac * t_ac**2)
		
		a_speed = topspeed - (topspeed * (a / 180))
		
		t_dec = (topspeed - a_speed) / dec
		dist_to_dec = (topspeed * t_dec) - (0.5 * dec * t_dec**2)
		
		DIST = l - dist_to_ac - dist_to_dec
		Time_to_Dist = DIST / topspeed
		
		TIME += t_ac + Time_to_Dist + t_dec
		SPEED = a_speed
		j += 2
	car_times[car_num] = round(TIME * 3600, 2)

C = {}
for k, v in car_times.items():
	C[v] = k
T = sorted(C)

for k in T:
	print C[k], k