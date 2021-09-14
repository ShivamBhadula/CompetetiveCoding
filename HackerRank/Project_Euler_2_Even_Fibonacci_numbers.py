#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n1=1
    n2=2
    n3=3
    sum=2
    while(n3<n):
        n1=n2
        n2=n3
        if(n3%2==0):
            sum+=n3
        n3=n1+n2
    print(sum)
        
        