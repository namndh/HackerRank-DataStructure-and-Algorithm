# https://www.hackerrank.com/challenges/compare-the-triplets

import sys

def solve(a0,a1,a2,b0,b1,b2):
    lst = [
        {1:a0,2:b0},
        {1:a1,2:b1},
        {1:a2,2:b2}
    ]
    comp_point = {1:0,2:0}
    for x in lst:
        if x[1] > x[2]:
            comp_point[1] = comp_point[1] + 1
        if x[1] < x[2]:
            comp_point[2] = comp_point[2] + 1
    result = []
    for x in xrange(1,3):
        result.append(comp_point[x])
    return result
result = solve(1,6,3,2,5,4)
print result
