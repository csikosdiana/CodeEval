data = ["m*M}Qz`\fz/We}e[`md;Puuat-;UP|Yi64iXh%{Hnul8&onq0p*mY+4x\/{ZTw[gXeJV2&.P*Ywe",
		"VA,8Z%z-AYzp6o{qeX3Q|\`Zw7{78:Y80qP-,b0BDVvZh60x59.0xe5.0x82.0xe1uptW8eF8C]nKJ9c(AtXa9>Dy}nF'Jr",
		"Cq2ox2Mmr7PuaPO023244514100.@({-mER/yhWg)wsf\"`Fu_tp.C]6$!?(^+wzLBxi,PJ41Hdu`m>Bz=v*^~N|h",
		"jfZ&y9w'XkrrO6JDoZOyZ864.599.341.917JBJ5u(^i%BjecAd\"$4UKtPnbtvx^01540.01127.0525.01625tU$HY/,Uw(/CJP]L+/XohV2hD&]",
		"9Pl.1011001111001011000001011100001,Y,HNAiSzL;?BU_UQlCvyzRU^\"R]{kVJ\"[+3%PK`]\"V?;Y'8CjJ<&QGmESP6W7&P,@$tFtL",
		"`z6DR}/>gLfLX[1&]Vr8\"EG-_+wy?sw4beHIp^oTtZzvWBwY{[89.229.130.225R,?B;\"?[ix4^9D$fVaJ_V\)N`B",
		"=ddalCNOM)FnA=/r,?}#idpo1E#eeMq.wyfu/2viz;c_[kHppMh,K|\`Q1_R(`jRNvCZW2Niz7Q#",
		"w:b21f[rsnj^Rgg[t!(<5v`Iup^&]o@489.229.130.225gw4\SwBEbN222.137.104.206[Jo<)lj36bB.034062405073xx37d;~wKi/D\"I'AeVfeBO",
		"|7$mi3k]f}9N*Vjq5aMy[Xd+3a$n$paB?5p9^01000000.11101110.00100000.01100101u@0:7&J;8FDZ<LuN-ecftQ%XU2urHk=N\"y}1Zt+",
		"|lLN|l8ZlMi()kN29/B!uj~l8#1o?Kcp/1{FfL]1/NsK$<@`)0P+LVgv4ziP>t840131.0345.0202.0341`}Z*Xz[8IH?'",
		"^~H5]JqL#?>d8V5JPP1101100000.1001010111.101010101.11100101011Funfr=3*E\pEa\"3YV^?J+;dLA#t)$3Lvi5J<MSF]LB&yOXgO't/E864.599.341.917Ze033642264316z~7",
		"W7+1&dt2#Ek&<am6G|!!18P>?|?qQyV(0k?>KPB:t{IRUm>cuN0^[YSOsixxF\"zzl5LALPIaXFM.",
		"jMfgpfH+w>M8\`r{;`XdEYm0Rc7o>Aqq4k?gP>,O^2I^]OF#zN\cLSUQ(x!(oxA0l<xjM=-qcIXE",
		"_L)a,<}f4u9dc]'440h0y7Yu=&NOfz-k%hk/FLpVZBsX|+P5YjaNBH]TCG~{,k]Dc\7p$)s&4D+Y",
		"xI~0JkBd]}c#]!4eGec7oz>d:yYl*K_AK^Hd_<c+hjD4w:-[90?}lBZ]^@iT2A&i9=9tsjg3muNC",
		",6ze^#eqtjrd`P&?WY,J-]L)_gVR*NJ~]Q(#l\"Yu~Jpl*ui\"9JtZ=&2B{!6\"iP@Y@3I%Zft>cpd`",
		"OwEK!d?y\M(_L~|=lm1++BLA<&PnOnBAfga>t},x{T$*&/}+wX{j/pm'|N~Cq1000000111011100010000001100101x~[*Scc=lb82`K~",
		"HydTS#@@864.599.341.917Q&.DVb\ails}C101100100110010011011000101110100&@KyFK\"7}u3\63?u][~zz>-r$_OqUbE*uv,\ccCnUmP\<p,o4E6[7c]",
		"v<md%aG2z8n'}\"9}qwZYnHdo>`4/Ht!3puL.A\'].BA>reos{U0x360.0x257.0x155.0x395y^UGXh^'`|I.CV}R>a}RAhO%Vw",
		"uQ#27/z^B8q:x(I|$k9dmF{\<ofV5sg[F>P(t!ui5[<mpXTzO%0wF|E2Sh6bl5[YZ:Tm%JsE*5pUO"]

import re
pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
Intruders = []
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	match = re.findall(pattern, test)
	if match != []:
		for m in match:
			Intruders.append(m[0])	
#test_cases.close()

#print Intruders
Max_count = 0
Max_intruder = ""
for i in Intruders:
	c = Intruders.count(i)
	if c > Max_count:
		Max_count = c
		Max_intruder = i
print Max_intruder