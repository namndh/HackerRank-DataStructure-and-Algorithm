#https://www.hackerrank.com/challenges/mini-max-sum

import sys

arr = map(int, raw_input().strip().split(' '))
arr.sort()
min_sum = 0
max_sum = 0
for x in xrange(0,4):
    min_sum = min_sum + arr[x]
for x in range(1,5):
    max_sum = max_sum + arr[x]
print min_sum,
print max_sum
