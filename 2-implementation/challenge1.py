# https://www.hackerrank.com/challenges/grading/problem


import sys

def solve(grades):
    for i in xrange(len(grades)):
        if grades[i] >= 38:
            num_teen = int(grades[i] / 10)
            num_unit = int(grades[i] % 10)
            diff = abs(num_unit - 5)
            if num_unit < 5:
                if diff < 3 :
                    grades[i] = num_teen*10 + 5
            if num_unit  > 5:
                if diff >=3 :
                    grades[i] = (num_teen + 1)*10

    return grades


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n"
print "\n".join(map(str, result))
