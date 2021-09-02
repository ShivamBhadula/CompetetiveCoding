def update(value,l1):
    minimum=min(l1)
    if minimum>=value:
        return 0
    else :
        return value-minimum
for i in range(int(input())):
    l2=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    value=l2[1]
    print(update(value,l1))