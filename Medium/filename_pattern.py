data = ["*7* johab.py gen_probe.ko palmtx.h macpath.py tzp dm-dirty-log.h bh1770.h pktloc faillog.8.gz zconf.gperf",
		"*[0123456789]*[auoei]* IBM1008_420.so zfgrep limits.conf.5.gz tc.h ilogb.3.gz limits.conf CyrAsia-TerminusBold28x14.psf.gz nf_conntrack_sip.ko DistUpgradeViewNonInteractive.pyc NFKDQC",
		"*.??? max_user_watches arptables.h net_namespace Kannada.pl menu_no_no.utf-8.vim shtags.1 unistd_32_ia32.h gettext-tools.mo ntpdate.md5sums linkat.2.gz",
		"*.pdf OldItali.pl term.log plymouth-upstart-bridge rand.so libipw.ko jisfreq.pyc impedance-analyzer xmon.h 1.5.0.3.txt bank",
		"g*.* 56b8a0b6.0 sl.vim digctl.h groff-base.conffiles python-software-properties.md5sums CountryInformation.py use_zero_page session-noninteractive d2i_RSAPublicKey.3ssl.gz container-detect.log.4.gz",
		"*[0123456789]* keyboard.h machinecheck 46b2fd3b.0 libip6t_frag.so timer_defs.h nano-menu.xpm NI vim-keys.conf setjmp.h memcg"]

import re
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
for test in data:
	test = test.strip("\n")
	if len(test) == 0:
		continue
	test = test.split(" ")
	pattern = test[0]
	files = test[1:]
	#print pattern
	FILENAME = []
	pattern = re.sub('\.', '\.', pattern)
	pattern = re.sub('\*', '.*', pattern)
	pattern = re.sub('\?', '.', pattern)
	for i in files:
		if re.match('^' + pattern + '$', i):
			FILENAME.append(i)
	if FILENAME == []:
		print "-"
	else:
		print " ".join(FILENAME)

#test_cases.close()