for i in range(int(input())):
    l,r,s=map(int,input().split())
    small=l//s
    if l%s!=0:
        if s*(small+1)<=r:
            small+=1
        else:
            small=-1
    if small==-1:
        big=-1
    else:
        big=r//s
        if big*s<l:
            big=-1
    print(small,big)