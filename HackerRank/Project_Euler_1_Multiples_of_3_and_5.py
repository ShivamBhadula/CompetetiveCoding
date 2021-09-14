#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    v3=(n-1)//3
    v5=(n-1)//5
    v15=(n-1)//15
    sum3=3*(v3*(v3+1))//2
    sum5=5*(v5*(v5+1))//2
    sum15=15*(v15*(v15+1))//2
    print(sum3+sum5-sum15)
