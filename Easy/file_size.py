import sys
file = sys.argv[1]
import os
print os.stat(file).st_size