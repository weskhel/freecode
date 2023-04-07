import sys
import math


#Given a string S print first occurrence of all the characters present in that order only.
#Input
#Line 1: An integer N for the number of strings to enter
#Next N lines: String S

#n = int(input())
#for i in range(n):
#    s = input()

n = int(input())
for i in range(n):
    a=[]
    s=input()
    for i in list(s):
        if i not in a:
            a.append(i)
    print("".join(a))


