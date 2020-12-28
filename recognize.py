import sys
from libs import load

fileCompare = sys.argv[1]
result = load.compare_pictures(fileCompare)
print(result)