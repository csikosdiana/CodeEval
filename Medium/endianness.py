import sys
def endianess():
    return sys.byteorder

E = endianess()
if E == "little":
    print "LittleEndian"
else:
    print "BigEndian"