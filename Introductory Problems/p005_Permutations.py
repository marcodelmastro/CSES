#!/usr/bin/env python3
n = int(input())
if n==2 or n==3:
    print("NO SOLUTION")
else:
    for j in (2,1):
        for i in range(j,n+1,2):
            print(i,end=" ")
    print()
