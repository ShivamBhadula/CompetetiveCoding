for _ in range(int(input())):
    k=int(input())
    dic = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}
    l1=list(map(int,input().split()))
    k=k%sum(l1)
    if k==0:
        for i in range(len(l1)):
            if l1[i]!=0:
                a=i
    else :
        for i in range(len(l1)):
            k-=l1[i]
            if k<=0:
                a=i
                break
    print(dic[a])