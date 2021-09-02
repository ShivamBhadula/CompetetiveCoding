size=int(input())
s1=input()
l1=[0,0,0,0,0,0,0]
for i in range(size):
    if s1[i]=='h':
        l1[0]+=1
    elif s1[i]=='a':
        l1[1]+=1
    elif s1[i]=='e':
        l1[2]+=1
    elif s1[i]=='r':
        l1[3]+=1
    elif s1[i]=='c':
        l1[4]+=1
    elif s1[i]=='k':
        l1[5]+=1
    elif s1[i]=='t':
        l1[6]+=1
l1[1]//=2
l1[2]//=2
l1[3]//=2
l1[0]//=2
print(min(l1))