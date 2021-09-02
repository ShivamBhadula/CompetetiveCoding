size=int(input())
s1=input()
s2=''
for i in s1:
    if i=='H':
        s2+='H'
    if i=='.':
        s2+='B'
if s2.find('HH')==-1:
    print('YES')
    print(s2)
else:
    print('NO')