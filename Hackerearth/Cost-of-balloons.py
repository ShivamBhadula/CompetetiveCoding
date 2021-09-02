t=int(input())
for i in range(t):
    c=list(input().split(' '))
    g=int(c[0])
    p=int(c[1])
    z=int(input())
    sumg=0
    sump=0
    for j in range(z):
        v=list(input().split(' '))
        sumg+=int(v[0])
        sump+=int(v[1])
    sum1=g*sumg+p*sump
    sum2=g*sump+p*sumg
    if sum1>=sum2:
        print(sum2)
    else:
        print(sum1)