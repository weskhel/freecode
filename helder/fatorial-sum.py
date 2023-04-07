import sys
import math
n = int(input())
s=0
i=2
while i*i<n:
     while n%i==0:
        s+=i
        n=n/i
     i=i+1
print(s+int(n))
