
from __future__ import print_function
print('one', 'two', 'three', sep='')
print (' ','#','#','#',sep='')
n = int(raw_input().strip())
for x in xrange(0,n):
    for i in range(0,n-1-x):
        print (' ',end=''),
    for j in range(0,x):
        print ('#',end='')
    print('#')
