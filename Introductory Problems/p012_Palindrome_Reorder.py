#!/usr/bin/env python3
from collections import Counter
s = input()
c = Counter(s)
odd = []
even = []
for l,n in c.items():
    if n%2==0:
        even.append(l)
    else:
        odd.append(l)
if len(odd)>1:
    print("NO SOLUTION")
else:
    p = ""
    for l in even:
        p += c[l]//2*l
    if len(odd):
        p += c[odd[0]]*odd[0]
    for l in even[::-1]:
        p += c[l]//2*l
    print(p)
