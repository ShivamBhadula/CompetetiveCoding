t=int(input())
while t!=0:
    t-=1
    i = 1
    n=int(input())
    for n in range(n,0,-1):
        print('*' * i  + '#' * (2 * (n-1)) + '*' * i)
        i+=1
 