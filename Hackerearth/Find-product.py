n=int(input())
x=input()
x=x.split(' ')
answer=1
for i in range(n):
    answer=(answer*int(x[i]))%(10**9+7)
print(answer)