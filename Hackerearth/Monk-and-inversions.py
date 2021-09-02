for _ in range(int(input())):
    length=int(input())
    l1=[]
    for i in range(length):
        l2=list(map(int,input().split()))
        l1.append(l2)
    count=0
    for i in range(length):
        for j in range(length):
            for k in range(i,length):
                for l in range(j,length):
                    if l1[i][j]>l1[k][l]:
                        count+=1
    print(count)