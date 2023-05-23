#!/usr/bin/env python3

def trailingZeros(n):
    t = 0
    k = 5
    while k<=n:
        t += len(range(k,n+1,k))
        k *=5
    return t

print(trailingZeros(int(input())))
