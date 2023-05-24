#!/usr/bin/env python3
n = int(input())
a = [int(i) for i in input().split(" ")]
s = 0
for i in range(1,len(a)):
    d = a[i-1]-a[i]
    if d>0:
        a[i] += d
        s += d
print(s)
