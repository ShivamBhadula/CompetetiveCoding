for _ in range(int(input())):
    size = int(input())
    l1 = list(map(int, input().split()))
    print(l1[0], end=' ')
    i=1
    while i< size:
        if l1[i]>l1[i-1]:
            print(l1[i],end=' ')
        else:
            if l1[i-1]%l1[i]==0:
                l1[i]=l1[i-1]
                print(l1[i],end=' ')
            else:
                l1[i]=l1[i]*((l1[i-1]//l1[i])+1)
                print(l1[i],end=' ')
        i+=1
    print()





