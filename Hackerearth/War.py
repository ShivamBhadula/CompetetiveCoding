test_case=int(input())
for _ in range(test_case):
    troops=int(input())
    level1=max(list(map(int,input().split())))
    level2=max(list(map(int,input().split())))
    if level1>level2:
        print("Bob")
    elif level1<level2:
        print("Alice")
    else:
        print('Tie')