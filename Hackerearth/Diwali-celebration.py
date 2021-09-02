test_case=int(input())
for _ in range(test_case):
    l=list(map(int,input().split()))
    original=l[0]
    daily=l[1]
    days=l[2]-1
    print(original+daily*days)