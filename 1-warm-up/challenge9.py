#https://www.hackerrank.com/challenges/time-conversion
import sys

# def timeConversion(s):
    # Complete this function
s = raw_input().strip()
print s
# result = timeConversion(s)
# print(result)
arr = s.split(":",2)
ex = arr[2]
if ex[2] == "A":
    if int(arr[0]) == 12:
        print "0" + ":" + arr[1] + ":" + ex[0] + ex[1]
    else:
        print arr[0] + ":" + arr[1] + ":" + ex[0] + ex[1]
if ex[2] == "P":
    if int(arr[0]) == 12:
        print "12" + ":" + arr[1] + ":" + ex[0] + ex[1]
    else:
        print str(int(arr[0])  + 12) + ":" + arr[1] + ":" + ex[0] + ex[1]
# print ex
# ex_arr = ex.split("P",1)
# print ex_arr
