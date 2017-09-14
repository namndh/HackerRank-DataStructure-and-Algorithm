#https://www.hackerrank.com/challenges/apple-and-orange/problem

import sys

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
apple_got = 0
orange_got = 0
for x in xrange(m):
    coor = a + apple[x]
    if s <= coor and coor <= t :
        apple_got = apple_got + 1
for x in xrange(n):
    coor = b + orange[x]
    if s <= coor and coor <= t:
        orange_got = orange_got + 1
print apple_got
print orange_got
