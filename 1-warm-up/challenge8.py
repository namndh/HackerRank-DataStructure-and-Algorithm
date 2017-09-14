#https://www.hackerrank.com/challenges/birthday-cake-candles

import sys

def birthdayCakeCandles(n, ar):
    from collections import Counter
    counter = Counter(ar)
    return counter[max(arr)]

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
