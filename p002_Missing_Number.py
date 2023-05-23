#!/usr/bin/env python3
n = int(input())
v = [int(i) for i in input().split(' ')]
print( (n*(n+1))//2-sum(v) )
