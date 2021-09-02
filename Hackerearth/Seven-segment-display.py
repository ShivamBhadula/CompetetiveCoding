sticks = {"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
N = int(input())
for _ in range(N):
    num = list(input())
    total = 0
    for i in num:
        total += sticks[i]
    if total %2==0:
        print("1"*(total//2))
    else:
        print("7"+"1"*(total//2-1))