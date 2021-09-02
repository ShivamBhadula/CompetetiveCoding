for _ in range(int(input())):
    length=int(input())
    l1=list(map(int,input().split()))
    l1.sort()
    xor=l1[0]^l1[1]
    for i in range(1,length-1):
                val= l1[i]^l1[i+1]
                xor=min(xor,val)
    print(xor)