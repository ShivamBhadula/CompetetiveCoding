N = int(input())
a = list(map(int, input().split()))
last = 0
current_slice = 1
while (last + current_slice + 1) < N:
    current_slice = current_slice + 1
    last = last + current_slice
 
s = sum(a[0:(last + 1)])
maximum = s
for start in range(1, N):
    
    if ((last + 1) < N):
        s = s - a[start - 1] + a[last + 1]
        last = last + 1
 
    else:
        s = s - a[start - 1] - sum(a[(last - current_slice + 2):(last + 1)])
        last = last - current_slice + 1
        current_slice = current_slice - 1
 
    if s > maximum:
        maximum = s
 
print(maximum)