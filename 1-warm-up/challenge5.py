from __future__ import division
# https://www.hackerrank.com/challenges/plus-minus
arr = [1,-5,9,0,0,6,-4,5,-6,-8]
temp = {1:0,2:0,3:0}
for x in arr:
    if x > 0:
        temp[1] = temp[1] + 1
    if x < 0:
        temp[2] = temp[2] + 1
    if x == 0:
        temp[3] = temp[3] + 1
for x in temp:
    print "{0:.6f}".format(temp[x]/len(arr))
