# https://www.hackerrank.com/challenges/diagonal-difference
# mang 2 chieu

a = [[1,5,6],[3,8,9],[6,8,4]]

n = 3
sum1 = 0
for x in xrange(0,n):
    sum1 = sum1 + a[x][x]
sum2 = 0
for x in xrange(0,n):
    sum2 = sum2 + a[n-1-x][x]
result = abs(sum1 - sum2)
print result
