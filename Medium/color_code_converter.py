data = ["(0.56,0.94,0.21,0.02)",
		"HSL(359,0,0)",
		"HSV(276,33,7)",
		"#cfa9c4"]

import colorsys
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.rstrip()
	RGB = "RGB("
	if test.startswith("("):
		code = test[1:-1].split(",")
		code = map(float, code)
		R = 255 * (1 - code[0]) * (1 - code[3])
		R = int(round(R, 0))
		
		G = 255 * (1 - code[1]) * (1 - code[3])
		G = int(round(G, 0))
		
		B = 255 * (1 - code[2]) * (1 - code[3])
		B = int(round(B, 0))
		
		RGB = RGB + ",".join([str(R), str(G), str(B)]) + ")"
	
	elif test.startswith("HSL"):
		code = test[4:-1].split(",")
		code = map(int, code)
		H = code[0] / float(360)
		S = code[1] / float(100)
		L = code[2] / float(100)
		R, G, B = colorsys.hls_to_rgb(H, L, S)
		R, G, B = int(round(R*255, 0)), int(round(G*255, 0)), int(round(B*255, 0))
		
		RGB = RGB + ",".join([str(R), str(G), str(B)]) + ")"
	
	elif test.startswith("HSV"):
		code = test[4:-1].split(",")
		code = map(int, code)
		H = code[0] / float(360)
		S = code[1] / float(100)
		V = code[2] / float(100)
		R, G, B = colorsys.hsv_to_rgb(H, S, V)
		R, G, B = int(round(R*255, 0)), int(round(G*255, 0)), int(round(B*255, 0))
		
		RGB = RGB + ",".join([str(R), str(G), str(B)]) + ")"
	
	elif test.startswith("#"):
		code = test[1:]
		HextoDec = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
						"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
		R = HextoDec[code[0]] * 16 + HextoDec[code[1]]
		G = HextoDec[code[2]] * 16 + HextoDec[code[3]]
		B = HextoDec[code[4]] * 16 + HextoDec[code[5]]
		
		RGB = RGB + ",".join([str(R), str(G), str(B)]) + ")"

	print RGB

#test_cases.close()