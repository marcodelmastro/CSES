#!/usr/bin/env python3
s = input()
c = s[0]
count = 1
imax = 1
for i in range(1,len(s)+1):
    n = s[i%len(s)]
    if n==" ":
        continue
    if n==c:
        count+=1
    else:
        c=n
        if count>imax:
            imax = count
        count = 1
if count>len(s):
    imax = len(s)
print(imax)
