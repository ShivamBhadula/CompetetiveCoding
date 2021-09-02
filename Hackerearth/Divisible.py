n=int(input())
x=input()
x=x.split(' ')
esum=0
osum=0
for i in range(n):
    if i%2==0:
        if i<n/2:
            esum+=int(x[i][0])
        else:
            esum+=int(x[i][-1])
    else:
        if i<n/2:
            osum+=int(x[i][0])
        else:
            osum+=int(x[i][-1])
if(esum-osum)%11==0:
    print('OUI')
else:
    print('NON')
 