for i in range(int(input())):
    l,r=map(int,input().split())
    count=0
    count = (r - l + 1) - (r - l + 1) // 4
 
    if ((l%4==0 and r%4==2) or (l%4==1 and r%4==2) or (l%4==1 and r%4==3) or (l%4==2 and r%4==0) or (l%4==2 and r%4==2) or (l%4==2 and r%4==3)):
        count-=1
    print(count)