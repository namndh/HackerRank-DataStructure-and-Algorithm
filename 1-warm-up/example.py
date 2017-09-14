for x in xrange(1,3):
    print x
arr = [1,2,3,6,7,3,4,7]
print max(arr)
from collections import Counter
print [ k for k, v in Counter(arr).items() if v > 1]
counter = Counter(arr)
print counter[max(arr)]
