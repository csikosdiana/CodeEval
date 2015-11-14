A = 'Hello Word'
A1 = str.split(A)
rev_A = A1[::-1]
print " ".join(rev_A)

#Python 2.7.3
#import sys
#test_cases = open(sys.argv[1], 'r')
#sentences = test_cases.readlines()
#for sentc in sentences:
#    S = str.split(sentc)
#    rev_S = S[::-1]
#    print " ".join(rev_S)

#test_cases.close()